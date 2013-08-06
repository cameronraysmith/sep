#!/bin/sh

# generate data for examples of four cycle graphs
# for graph names
# see http://www.graphclasses.org/smallgraphs.html#nodes4

rm fourgraphs.data
touch fourgraphs.data
python minineqrep.py twok2 VERTICES >> fourgraphs.data
python minineqrep.py claw VERTICES >> fourgraphs.data
python minineqrep.py P4 VERTICES >> fourgraphs.data
python minineqrep.py C4 VERTICES >> fourgraphs.data
python minineqrep.py paw VERTICES >> fourgraphs.data
python minineqrep.py diamond VERTICES >> fourgraphs.data
python minineqrep.py K4 VERTICES >> fourgraphs.data

grep --no-group-separator -A1 'Name\|Volume ratio' fourgraphs.data | grep -v 'Name\|Volume ratio' > fourgraphs.summary
