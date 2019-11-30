debug_on = False
debug_fine_on = False

from copy import copy
import sys

def debug(msg):
    if debug_on:
        print(msg, file=sys.stderr)
    else:
        pass

def debug_fine(msg):
    if debug_fine_on:
        print(msg, file=sys.stderr)
    else:
        pass

def possible_givers(participants, chosen):
    # rule 4 - participants give one gift only
    possible_givers = copy(participants)
    for giver in map(lambda x: x[0], chosen):
        possible_givers.remove(giver)
    return possible_givers

def possible_recipients(giver, participants, chosen, last_years_pairs, families):
    """Exclude all rule-breaking recipients and return whatever's left, if
    anything."""

    possible_recipients = copy(participants)

    # rule 3 - can't choose yourself
    possible_recipients.remove(giver)

    # rule 1 - different pairing than last year
    for tmp_giver, recipient in last_years_pairs:
        if tmp_giver == giver and (giver, recipient) in last_years_pairs \
                and recipient in possible_recipients:
            debug_fine("%s gave to %s last year, excluding" % (giver, recipient))
            possible_recipients.remove(recipient)

    # rule 2 - give outside nuclear family
    for family in families:
        if giver in family:
            for recipient in family:
                if recipient in possible_recipients:
                    debug_fine("%s and %s are family, excluding" % (giver, recipient))
                    possible_recipients.remove(recipient)

    # rule 5 - participants receive one gift only
    for pair in chosen:
        if pair[1] in possible_recipients:
            debug_fine("%s is already paired, excluding" % pair[1])
            possible_recipients.remove(pair[1])

    return possible_recipients
