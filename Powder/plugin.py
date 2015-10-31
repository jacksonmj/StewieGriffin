###
# Copyright (c) 2011, AntB
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#	 this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#	 this list of conditions, and the following disclaimer in the
#	 documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#	 contributors to this software may be used to endorse or promote products
#	 derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import supybot.ircmsgs as ircmsgs
import json,random,urllib,re

class Powder(callbacks.PluginRegexp):
	"""Contains all sorts of random stuff."""
	threaded = True
	unaddressedRegexps = ['powderSnarfer','forumSnarfer']

	def browse(self, irc, msg, args, ID, blurb):
		"""<SaveID>

			Returns information about a save."""
		self._getSaveInfo(irc, ID, 0)
	browse = wrap(browse,['somethingWithoutSpaces',optional('text')])

	def oldbrowse(self, irc, msg, args, ID, blurb):
		"""<SaveID>

			Returns information about a save."""
		self._getOldSaveInfo(irc, ID, 0)
	oldbrowse = wrap(oldbrowse,['somethingWithoutSpaces',optional('text')])

	def powderSnarfer(self, irc, msg, match):
		r"http://powdertoy.co.uk/Browse/View.html\?ID=([0-9]+)|^[~]([0-9]+)|http://tpt.io/~([0-9]+)|http://powdertoy.co.uk/~([0-9]+)"
		ID = match.group(1) or match.group(2) or match.group(3) or match.group(4) 

		if msg.args[1].startswith("Save "+ID+" is"):
			return # Don't respond to save info from other bots with this plugin

		self.log.info("powderSnarfer - save URL Found "+match.group(0))
		if(match.group(0)[0]=="~"):
			self._getSaveInfo(irc, ID, 0)
		else:
			self._getSaveInfo(irc, ID, 1)
			
	powderSnarfer = urlSnarfer(powderSnarfer)

	def _getSaveInfo(self, irc, ID, urlGiven):
		ID = str(int(ID))
		data = json.loads(utils.web.getUrl("http://powdertoy.co.uk/Browse/View.json?ID="+ID))
		if(data["Username"]=="FourOhFour"):
			saveMsg = "Save "+ID+" doesn't exist."
		else:
			saveMsg = "Save "+ID+" is "+data["Name"].replace('&#039;','\'').replace('&gt;','>')+" by "+data["Username"]+". Score: "+str(data["Score"])+"."
			if(not urlGiven):
				saveMsg+=" http://tpt.io/~"+ID
		irc.reply(saveMsg,prefixNick=False)

	def _getOldSaveInfo(self, irc, ID, urlGiven):
		ID = str(int(ID))
		try:
			data = json.loads(utils.web.getUrl("http://powdertoythings.co.uk/OldPowder/Browse/View.json?ID="+ID))
		except:
			irc.reply("Old save "+ID+" doesn't exist.",prefixNick=False)
			return
		if(not data or data["Username"]=="FourOhFour"):
			saveMsg = "Old save "+ID+" doesn't exist."
		else:
			saveMsg = "Old save "+ID+" is "+data["Name"].replace('&#039;','\'').replace('&gt;','>')+" by "+data["Username"]+". Score: "+str(data["Score"])+"."
			if(not urlGiven):
				saveMsg+=" http://powdertoythings.co.uk/OldPowder/Saves/"+ID+".html"
		irc.reply(saveMsg,prefixNick=False)

	def frontpage(self,irc,msg,args):
		"""

		Returns the front page of saves via notices - abuse will not be tolerated."""
		data = json.loads(utils.web.getUrl('http://powdertoy.co.uk/Browse.json'))['Saves']

		outMsg = ''
		x=0
		for each in data:
			outMsg='{0}\x02Save:\x02 {1:<24} - \x02By:\x02 {2:<14} - \x02ID: \x02{3:<6} - \x02Votes:\x02 {4:<4}'.format(outMsg,each['Name'].replace('&#039;','\''),each['Username'],str(each['ID']),str(each['Score']))
			x+=1
			if x%2 is 0:
				irc.queueMsg(ircmsgs.privmsg(msg.nick,outMsg))
				outMsg=''
				continue
			outMsg='{0} -- '.format(outMsg)

	#	irc.queueMsg(ircmsgs.privmsg(msg.nick,outMsg))
	frontpage = wrap(frontpage)

	def forumSnarfer(self,irc,msg,match):
		r"http://powdertoy[.]co[.]uk/Discussions/Thread/View[.]html[?]Thread=([0-9]+)|http://tpt.io/:([0-9]+)"
		threadNum = match.group(1) or match.group(2)
		self.log.info("Forum thread found.")

		data = json.loads(utils.web.getUrl("http://powdertoy.co.uk/Discussions/Thread/View.json?Thread=%s"%(threadNum)))
		cg = data["Info"]["Category"]
		tp = data["Info"]["Topic"]

		irc.reply("Forum post is \"%s\" in the %s section, posted by %s and has %s replies. Last post was by %s at %s"%
				(tp["Title"],cg["Name"],tp["Author"],tp["PostCount"]-1,tp["LastPoster"],tp["Date"]),prefixNick=False)
	forumSnarfer = urlSnarfer(forumSnarfer)

	def profile(self, irc, msg, args, user):
		"""<username|ID>

		  returns a link to the users profile and some brief information"""

		try:
			userPage = utils.web.getUrl("http://powdertoy.co.uk/User.html?Name="+user)
			userID = userPage.split("<a href=\"/User.html?ID=")[1].split("\"")[0];
			userData = json.loads(utils.web.getUrl("http://powdertoy.co.uk/User.json?Name="+user))
			uDu = userData['User']
			irc.reply('http://tpt.io/@{0} | ID {1} | Has {2} saves - Average score {3} - Highest score {4} | Posted {5} topics -  {6} posts - Has {7} reputation.'.format(user,userID,uDu['Saves']['Count'],uDu['Saves']['AverageScore'],uDu['Saves']['HighestScore'],uDu['Forum']['Topics'],uDu['Forum']['Replies'],uDu['Forum']['Reputation']), prefixNick=False)

		except Exception, e:
			try:
			  	userPage = utils.web.getUrl("http://powdertoy.co.uk/User.html?ID="+user)
				userName = userPage.split("<h1 class=\"SubmenuTitle\">")[1].split("</h1>")[0]
				userData = json.loads(utils.web.getUrl("http://powdertoy.co.uk/User.json?ID="+user))
				uDu = userData['User']
				irc.reply('http://tpt.io/@{1} | ID {0} | Has {2} saves - Average score {3} - Highest score {4} | Posted {5} topics -  {6} posts - Has {7} reputation.'.format(user,userName,uDu['Saves']['Count'],uDu['Saves']['AverageScore'],uDu['Saves']['HighestScore'],uDu['Forum']['Topics'],uDu['Forum']['Replies'],uDu['Forum']['Reputation']), prefixNick=False)

			except Exception, e:
				irc.reply("User or ID doesn't exist - or Xeno screwed it again... {}".format(e))
				
		finally:
			return None

	profile = wrap(profile,['something'])

	def randomsave(self,irc,msg,args):
		"""

		Returns a random save from powdertoy.co.uk"""
		found = False
		while found is False:
			saveID = str(json.loads(utils.web.getUrl("http://powdertoythings.co.uk/Powder/Saves/Random.json?Count=1"))['Saves'][0]['ID'])
			page = json.loads(utils.web.getUrl("http://powdertoy.co.uk/Browse/View.json?ID="+saveID))
			if(page["Username"]!="FourOhFour"):
				found = True

		self._getSaveInfo(irc,saveID,0) 
	randomsave = wrap(randomsave)

	def comic(self,irc,msg,args):
		"""
		
		Returns latest comic number and name."""
		try:
			try:
				data = utils.web.getUrl("http://cate.superdoxin.com/")
			except:
				irc.error("Could not access comics website")
				return
			match = None
			for match in re.finditer(r" href=\"http://superdoxin.com/static/cate/files/(([0-9]+)([^\"]+))\"", data):
				pass
			filename = match.group(1)
			num = match.group(2)
			name = match.group(3)
			
			irc.reply("Latest comic id is {} and is titled {} - http://www.superdoxin.com/static/cate/files/{}".format(num,name,filename))
		except:
			irc.error("Comic checker is broken, use $bug comic")
	comic = wrap(comic)
Class = Powder

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
