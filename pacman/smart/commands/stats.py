#
# Copyright (c) 2004 Conectiva, Inc.
#
# Written by Gustavo Niemeyer <niemeyer@conectiva.com>
#
# This file is part of Smart Package Manager.
#
# Smart Package Manager is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# Smart Package Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Smart Package Manager; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
from smart.util.strtools import sizeToStr
from smart.option import OptionParser
from smart import *
import re

USAGE=_("smart stats")

DESCRIPTION=_("""
This command will show some statistics.
""")

EXAMPLES=_("""
smart stats 
""")

def parse_options(argv):
    parser = OptionParser(usage=USAGE,
                          description=DESCRIPTION,
                          examples=EXAMPLES)
    opts, args = parser.parse_args(argv)
    opts.args = args
    return opts

def main(ctrl, opts, reloadchannels=True):

    if reloadchannels:
        ctrl.reloadChannels()

    cache = ctrl.getCache()

    print _("Installed Packages:"), len([pkg for pkg in cache.getPackages()
                                              if pkg.installed])
    print _("Total Packages:"), len(cache.getPackages())
    print _("Total Provides:"), len(cache.getProvides())
    print _("Total Requires:"), len(cache.getRequires())
    print _("Total Upgrades:"), len(cache.getUpgrades())
    print _("Total Conflicts:"), len(cache.getConflicts())

# vim:ts=4:sw=4:et
