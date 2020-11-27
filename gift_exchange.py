#!/usr/bin/python3

# gift-exchange - Gift Exchange Name Matcher
# Copyright (C) 2020 Adam Monsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#############
# Rules:
# 1. give to a different person than last year
# 2. partners can't be nuclear family members
# 3. can't choose yourself
# 4. participants give one gift only
# 5. participants receive one gift only
#############

import importlib
import libgiftex
import pprint
import random
import sys
import time

_suspensefulDelay = 5

try:
    from halo import Halo
    foundHalo = True
except ImportError:
    foundHalo = False

if __name__ == '__main__':
    from data import participants, last_years_pairs, families

    chosen = []

    pleaseWait = 'Please Wait! The robot is picking numbers out of a hat...'
    if foundHalo:
        with Halo(text=pleaseWait, spinner='earth'):
            time.sleep(_suspensefulDelay)
    else:
        print(pleaseWait)
        time.sleep(_suspensefulDelay)

    while len(chosen) != len(participants):
        givers = libgiftex.possible_givers(participants, chosen)
        # if we omit randomization here, our "abort/retry" (below) may fail,
        # although I'm not really sure why
        giver = random.choice(givers)
        libgiftex.debug_fine("GIVER: %s" % giver)
        recipients = libgiftex.possible_recipients(giver, participants, \
                chosen, last_years_pairs, families)
        # brute force abort/retry
        if len(recipients) == 0:
            libgiftex.debug("No recipients, trying a different giver...")
            if len(givers) <= 1:
                libgiftex.debug("No other givers to try! Starting over...")
                chosen = []
            if len(givers) == 2:
                libgiftex.debug("Stalemate! Two givers left but they can't give to eachother. Starting over...")
                chosen = []
            continue
        recipient = random.choice(recipients)
        libgiftex.debug_fine("RECIPIENT: %s" % recipient)
        chosen.append( (giver, recipient) )
        libgiftex.debug("PAIRS ARE NOW: %s" % chosen)

    chosen.sort()

    participants.sort()
    families.sort()

    f = open('data.py', 'w')
    f.write("participants = ")
    f.write(pprint.pformat(participants))
    f.write("\n\n")
    f.write("# OK to include folks from last year not in this year\n")
    f.write("last_years_pairs = ")
    f.write(pprint.pformat(chosen))
    f.write("\n\n")
    f.write("# groups of people that shouldn't give to one another\n")
    f.write("families = ")
    f.write(pprint.pformat(families))
    f.write("\n")
    f.close()

    for giver, recipient in chosen:
        print("{} gives to {}".format(giver, recipient))
        shuffling = 'Shuffling...'
        if foundHalo:
            with Halo(text=shuffling, spinner='moon'):
                time.sleep(_suspensefulDelay)
        else:
            print(shuffling)
            time.sleep(_suspensefulDelay)
