#!/bin/sh

# generate data for examples of four cycle graphs
# for graph names
# see http://www.graphclasses.org/smallgraphs.html#nodes4

rm fourgraphs.data
touch fourgraphs.data

# binary graphs
python minineqrep.py twok2 VERTICES >> fourgraphs.data
python minineqrep.py claw VERTICES >> fourgraphs.data
python minineqrep.py P4 VERTICES >> fourgraphs.data
python minineqrep.py C4 VERTICES >> fourgraphs.data
python minineqrep.py paw VERTICES >> fourgraphs.data
python minineqrep.py diamond VERTICES >> fourgraphs.data
python minineqrep.py K4 VERTICES >> fourgraphs.data

# hypergraphs
#python minineqrep.py flagpole VERTICES >> fourgraphs.data
python minineqrep.py basket VERTICES >> fourgraphs.data
python minineqrep.py tripod VERTICES >> fourgraphs.data
#python minineqrep.py overtwo VERTICES >> fourgraphs.data
python minineqrep.py overtwoconnect VERTICES >> fourgraphs.data
python minineqrep.py overthree VERTICES >> fourgraphs.data

grep --no-group-separator -A1 'Name\|Volume ratio' fourgraphs.data | grep -v 'Name\|Volume ratio' > fourgraphs.summary
