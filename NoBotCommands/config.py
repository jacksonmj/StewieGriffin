###
# Copyright (c) 2015, jacksonmj
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('NoBotCommands')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('NoBotCommands', True)


NoBotCommands = conf.registerPlugin('NoBotCommands')
conf.registerChannelValue(NoBotCommands, 'badPrefix',
    registry.Regexp(r'/^([^a-zA-Z0-9]+)/', _("""Regex to match the beginning of a line which will trigger other bots""")))
conf.registerChannelValue(NoBotCommands, 'badSuffix',
    registry.Regexp('/$/', _("""Regex to match the end of a line which will trigger other bots""")))



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
