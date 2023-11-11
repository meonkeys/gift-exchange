# gift exchange

Use this simple command-line utility to transform the social experience of drawing names out of a hat into a streamlined, people-free robotic randomized exercise of the Internet age!

## Prerequisites

Required:

* Python 3.4+

Optional:

* [halo](https://pypi.org/project/halo/) - for fancy "waiting..." spinners

## Usage

1. Clone this repository.
1. Edit `data.py` with the names of the participants of your drawing, pairs from the previous drawing (if applicable), and families.
1. Run `gift_exchange.py`. Matches will be printed to standard output and `data.py` will be updated in place.
1. Profit!

## Gifting rules

Logic for who can give to whom are found in `libgiftex.py`. They are:

1. Different pairing than last year.
2. Pair outside nuclear families (per `families` in the data file).
3. Can't choose yourself.
4. Participants give one gift only.
5. Participants receive one gift only.

## Copyright, License

Copyright (C) 2010-2023 Adam Monsen

Available free of charge under the AGPLv3. See COPYING for the full license text.
