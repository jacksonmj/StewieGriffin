###
# Copyright (c) 2015, jacksonmj
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
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
import re
import json
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('GithubInfo')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class GithubInfo(callbacks.Plugin):
    """Fetch info from github"""
    threaded = True

    def _outputLatestCommitInfo(self, irc, user, repo, branch):
        """Reply with info about latest commit, returns true if successful"""
        self.log.info("GithubInfo: trying: {} {} {}".format(user,repo,branch))
        if not branch:
            try:
                url = "https://api.github.com/repos/{0}/{1}".format(user,repo)
                data = json.loads(utils.web.getUrl(url).decode('UTF-8'))
                branch = data['default_branch']
            except:
                return False
        url = "https://api.github.com/repos/{0}/{1}/branches/{2}".format(user,repo,branch)
        try:
            data = json.loads(utils.web.getUrl(url).decode('UTF-8'))
            data = data['commit']['commit']

            when = data["committer"]["date"].split("T")
            msg = data["message"].replace("\n"," ")
            msg = re.sub(r'\s{2,}', '  ', msg)

            irc.reply("Last commit to {user}'s {repo} repo, {branch} branch, was by {committer} on {commitdate} at {committime}. Commit message was \"{commitmsg}\" - https://github.com/{user}/{repo}/tree/{branch}".format(
                user=user, repo=repo, branch=branch,
                committer=data["committer"]["name"],
                commitdate=when[0], committime=when[1].rstrip("Z"),
                commitmsg=msg), prefixNick=False)
            return True
        except:
            return False
        return False

    def git(self, irc, msg, args, user, repo, branch):
        """[username [repo] [branch]]

        Returns information about the latest commit in a github repo. username and repo can only be omitted if defaults are set in config. Arguments are CaSe-SeNsItIvE"""

        if user and user.lower() in ["simon", "isimon", "ximon"]:
            user="simtr"
        if not user:
            user = self.registryValue('defaultUser', msg.args[0])
        if not user:
            irc.error("Username not specified and no default set.")
            return

        defaultRepo = self.registryValue('defaultRepo', msg.args[0])
        defaultBranch = self.registryValue('defaultBranch', msg.args[0])
        if not repo:
            if not defaultRepo:
                irc.error("Repository not specified and no default set.")
                return
            if defaultBranch and branch is None:
                if self._outputLatestCommitInfo(irc, user, defaultRepo, defaultBranch):
                    return
            if self._outputLatestCommitInfo(irc, user, defaultRepo, branch):
                return
            irc.error("HTTP 404. Please check and try again.")
            return

        if not branch:
            # Args: username branch, so repo is actually the branch
            if defaultRepo:
                if self._outputLatestCommitInfo(irc, user, defaultRepo, repo):
                    return

            # Args: username repo
            if defaultBranch:
                if self._outputLatestCommitInfo(irc, user, repo, defaultBranch):
                    return
            if self._outputLatestCommitInfo(irc, user, repo, ''):
                return

            irc.error("HTTP 404. Please check and try again.")
            return

        if self._outputLatestCommitInfo(irc, user, repo, branch):
            return
        irc.error("HTTP 404. Please check and try again.")

    git = wrap(git,[optional('somethingWithoutSpaces'),optional('somethingWithoutSpaces'),optional('somethingwithoutspaces')])


Class = GithubInfo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
