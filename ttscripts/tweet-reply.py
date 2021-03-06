#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l == 1:
    sa1 = input("* Twitter ID for status being replied to: ")
    stat = sa1.split("/")[-1]
    mesg = input("* Status update (140 characters max, must include @username): ")
elif l == 2:
    sa1 = sys.argv[1]
    sa = sa1.split("/")
    stat = sa[-1]
    if sa1.startswith("https://twitter.com/") is True:
        user = sa[2]
        char = 140 - (len(user) + 2)
        msg = input("Enter the reply, not counting the username ({0} characters max): ".format(char))
        mesg = "@" + user + " " + msg
    else:
        stat = sys.argv[1]
        mesg = input("* Status update (140 characters max, must include @username): ")
elif l >= 3:
    sa1 = sys.argv[1]
    sa = sa1.split("/")
    stat = sa[-1]
    msg = []
    for i in range(l - 2):
        msg.append(str(sys.argv[i + 2]))
    mesg = " ".join(msg)
else:
    stat = input("* Twitter ID for status being replied to: ")
    mesg = input("* Status update (140 characters max, must include @username): ")

try:
    twitter.update_status(status=mesg, in_reply_to_status_id=stat)
except TwythonError as e:
    print(e)
