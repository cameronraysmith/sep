from kcfromgraph import *
from minineqrep import *

from graphlist4 import graphdict
graphdict["C3"] = [(0, 1), (1, 2), (2, 0)]

minineqs, dim = minineqgen("C3")

polyproperty = "VERTICES"
eqfname = "C3"

volkolmogorov = runpolymakescript(minineqs,
                                  "INEQUALITIES",
                                  "INEQUALITIES",
                                  eqfname)

polyout = runpolymakescript(minineqs,
                            "INEQUALITIES",
                            polyproperty,
                            eqfname)

boolepolyverts = booleverts(polyout)

volboole = runpolymakescript(boolepolyverts,
                             "POINTS",
                             "FACETS",
                             eqfname)

print "KC inequalities/facets"
print volkolmogorov
print ""

print "BP inequalities/facets"
print volboole
print ""

extraineqs = [x for x in volboole.split('\n') if x not in volkolmogorov.split('\n')]

print "BP inequalities not in KC"
print '\n'.join(extraineqs)
print ""

# Eliminated variables

# Edges
# [[0, 1], [0, 1], [0, 1], [1, 2], [1, 2], [2, 0]]
# States
# [[0, 0], [0, 1], [1, 0], [0, 0], [0, 1], [0, 0]]

# Remaining variables

# Edges
# [[0, 1], [1, 2], [1, 2], [2, 0], [2, 0], [2, 0]]
# States
# [[1, 1], [1, 0], [1, 1], [0, 1], [1, 0], [1, 1]]

# Each line describes one linear inequality.
# The encoding is as follows:
# (a_0,a_1,...,a_d) is the inequality a_0 + a_1 x_1 + ... + a_d x_d >= 0.

# KC inequalities/facets
# 1 1 -1 -1 -1 0 -1
# 0 -1 1 1 0 0 0
# 0 -1 0 0 1 0 1
# 1 0 -1 0 0 -1 -1
# 0 0 0 -1 0 1 1
# 1 0 0 0 -1 -1 -1
# 0 1 0 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 1 0 0 0
# 0 0 0 0 1 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0

# BP inequalities/facets
# 0 1 0 -1 0 1 0
# 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0
# 0 1 0 0 0 0 0
# 1 1 -1 0 -1 -1 -1
# 1 0 0 0 -1 -1 -1
# 1 0 -1 0 0 -1 -1
# 1 1 -1 -1 -1 0 -1
# 0 0 0 1 0 0 0
# 0 0 0 0 0 0 1
# 0 -1 1 1 0 0 0
# 0 -1 1 0 0 0 1
# 0 -1 0 1 1 0 0
# 0 0 0 0 0 1 0
# 0 -1 0 0 1 0 1
# 0 0 0 -1 0 1 1

# BP inequalities not in KC
# 0 1 0 -1 0 1 0
# 1 1 -1 0 -1 -1 -1
# 0 -1 1 0 0 0 1
# 0 -1 0 1 1 0 0

