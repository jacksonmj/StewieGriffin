###
# Copyright (c) 2011, Anthony Boot
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import supybot.schedule as schedule
import random,time,json


class CustOps(callbacks.Plugin):
 """Custom op commands."""
 threaded = True

 random.seed()
 for each in range(0,random.randint(50,100)): i = random.random()
 del i

 def ninja(self,irc,msg,args,channel,user,reason):
  """<user> [reason]

  Forces a user to part the channel. Essentially a kick without the counter."""
  if not reason:
   reason = '{} says GTFO.'.format(msg.nick)

  irc.queueMsg(ircmsgs.IrcMsg('REMOVE {} {} :{}'.format(channel,user,reason)))
 ninja = wrap(ninja,['op',('haveOp','remove a user from the channel'),'nickInChannel',additional('text')])

 def social(self,irc,msg,args,channel,user,junk):
  """[#powder] <user> 

  Sets a redirection ban from #powder to #powder-social, kicks the user (exploiting a users auto-rejoin to force them to #powder-social) then lifts the ban. Also sends the user a notice informing them of what happened."""
  if channel not in '#powder': channel = '#powder'
  irc.queueMsg(ircmsgs.IrcMsg('MODE #powder +b {}$#powder-social'.format(irc.state.nickToHostmask(user))))
  irc.queueMsg(ircmsgs.IrcMsg('KICK #powder {} :Take it to #powder-social'.format(user)))
  irc.queueMsg(ircmsgs.invite(user,'#powder-social'))
  irc.queueMsg(ircmsgs.IrcMsg('NOTICE {} :{} has requested you take your current conversation to #powder-social.'.format(user,msg.nick)))
  expires = time.time()+300
  def f():
   irc.queueMsg(ircmsgs.IrcMsg('MODE #powder -b {}$#powder-social'.format(irc.state.nickToHostmask(user))))
  schedule.addEvent(f,expires)

#  irc.queueMsg(ircmsgs.IrcMsg('MODE #powder -b {}$#powder-social'.format(irc.state.nickToHostmask(user))))
 social = wrap(social,['op',('haveOp','Evict a user to #powder-social'),'nickInChannel',optional('anything')])

 def stab(self,irc,msg,args,channel,user,timer,reason):
  """<user> [seconds] [reason (ignored)]

  Stabs a user, putting them on quiet for a random time up to 10 mins."""

  hmask = irc.state.nickToHostmask(user)
  hostmask = ircutils.joinHostmask('*', '*', ircutils.hostFromHostmask(hmask))
  irc.queueMsg(ircmsgs.IrcMsg('MODE {0} +q {1}'.format(channel,hostmask)))

  t = time.time()
  r = timer
  if not r > 0:
   r = random.randint(30,600)
  expires = t+r

  len={}
  len['m'] = len['s'] = 0

  while r > 59:
   len['m']+=1
   r-=60

  len['s'] = r 

  irc.queueMsg(ircmsgs.IrcMsg('NOTICE {0} :{1} has been quieted for {2}:{3:0>2}'.format(msg.nick,user,len['m'],len['s'])))
  def f():
   irc.queueMsg(ircmsgs.IrcMsg('MODE {0} -q {1}'.format(channel,hostmask)))
  schedule.addEvent(f,expires)
  irc.noReply()
 stab = wrap(stab,['op',('haveOp','Quiet a user'),'nickInChannel',optional('int'), optional('text')])

 def unstab(self,irc,msg,args,channel,user):
  """<user>
  
  Removes +q from a user in channel"""
  hmask = irc.state.nickToHostmask(user)
  hostmask = ircutils.joinHostmask('*', '*', ircutils.hostFromHostmask(hmask))
  irc.queueMsg(ircmsgs.IrcMsg('MODE {} -q {}'.format(channel,hostmask)))
 unstab = wrap(unstab,['op',('haveOp','Set user modes'), 'nickInChannel'])
 
 def setinfo(self,irc,msg,args,channel,user,infoline):
  """\x02<user> <infoline>\x02

  Allows an op to set an info line about a user."""
  #if msg.nick.lower() is user.lower(): irc.error('Nice try')
  try: self.infoLines
  except: self._getInfo()

  try: self.infoLines[user.lower()]
  except: self.infoLines[user.lower()]={}

  if infoline!='':
   self.infoLines[user.lower()][msg.nick.lower()]=infoline
  else:
   del self.infoLines[user.lower()][msg.nick.lower()]
  with open('INFOLINES','w') as f:
    f.write(json.dumps(self.infoLines,sort_keys=True,indent=4))
  irc.replySuccess('| Infoline added')
 setinfo = wrap(setinfo, ['op',('haveOp','Set info lines'), 'nick', 'text'])

 def _getInfo(self):
#  try:
   with open('INFOLINES','r') as f:
    self.infoLines=json.load(f)
#  except:
#   self.infoLines={}
#   with open('INFOLINES','w') as f:
#    json.dump(self.infoLines,f)


 def info(self,irc,msg,args,user,op):
  """\x02<user>\x02

  Shows a users infoline at random (if set)"""
  try: self.infoLines
  except: self._getInfo()

  if not user: user = msg.nick

  try: i = self.infoLines[user.lower()]
  except:
   irc.error('No info for that user in DB')
   return
  if not len(self.infoLines[user.lower()]):
   irc.error('No info for that user in DB')
   return

  if not op:
   op = random.choice(list(self.infoLines[user.lower()]))
  op=op.lower()
  if 'all' in op:
   msg = ''
   for each in self.infoLines[user.lower()]:
    msg+=' By {0} -> "{1}" '.format(each.capitalize(),self.infoLines[user.lower()][each].replace('"','').replace('\'',''))
   irc.reply(msg,prefixNick=False)
   return 0

  try: irc.reply('{0} by {1} -> {2}'.format(user, op.capitalize(), self.infoLines[user.lower()][op]), prefixNick=False)
  except: irc.error('{0} hasn\'t provided an infoline for {1} or isn\'t an op'.format(op,user))
 info = wrap(info,[optional('nick'),optional('nick')])

 def selfInfo(self,irc,msg,args,line):
  """<string>

  Lets you set your own info line"""
  try: i = self.infoLines[msg.nick.lower()]
  except: self._getInfo()

  try: self.infoLines[msg.nick.lower()]
  except: self.infoLines[msg.nick.lower()]={}
  
  self.infoLines[msg.nick.lower()][msg.nick.lower()]=line
  if line!='': 
   irc.reply('Personal info line added')
  else:
   del self.infoLines[msg.nick.lower()][msg.nick.lower()]
   irc.reply('Personal info line deleted')
  with open('INFOLINES','w') as f:
   f.write(json.dumps(self.infoLines,sort_keys=True,indent=4))
 selfinfo = wrap(selfInfo,['text'])
Class = CustOps


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
