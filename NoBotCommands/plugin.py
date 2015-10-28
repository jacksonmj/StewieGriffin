###
# Copyright (c) 2015, jacksonmj
# All rights reserved.
#
#
###

import supybot.log as log
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import re
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('NoBotCommands')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class NoBotCommands(callbacks.Plugin):
    """Filter output to avoid sending commands to other bots"""

    def callPrecedence(self, irc):
        return ([], [cb for cb in irc.callbacks if cb is not self and cb.__class__.__name__ not in ['Owner']])

    def outFilter(self, irc, msg):
        if msg.command == 'PRIVMSG' and not ircmsgs.isCtcp(msg):
            text = msg.args[1]
            strippedText = ircutils.stripFormatting(text)

            def stripStringL(txt):
                return self.registryValue('badPrefix', msg.args[0]).sub('',txt)
            def stripStringR(txt):
                return self.registryValue('badSuffix', msg.args[0]).sub('',txt)
            if stripStringL(strippedText) != strippedText:
                text = ' ' + text
            if stripStringR(strippedText) != strippedText:
                text = text + '.'

            newArgs = list(msg.args)
            newArgs[1] = text
            return ircmsgs.IrcMsg(msg=msg, args=tuple(newArgs))
        return msg

Class = NoBotCommands


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
