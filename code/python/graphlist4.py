"""
A subset of the non-isomorphic graphs on 4 nodes

enumerate non-isomorphic graphs
on 4 vertices
http://math.stackexchange.com/questions/100560/enumerate-non-isomorphic-graphs-on-n-vertices
http://www.roard.com/docs/cookbook/cbsu5.html
https://oeis.org/A000088/a000088a.gif
http://www.graphclasses.org/smallgraphs.html#nodes4
http://www.artofproblemsolving.com/Wiki/index.php/Burnside's_Lemma
"""

# 2K2 = \bar{C4}
twok2 = [(0,1),(2,3)]

# claw = K_{1,3}
claw = [(0,1),(0,2),(0,3)]

# P4 = 4-chain
P4 = [(0,1),(1,2),(2,3)]

# C4 = K_{2,2}
#edgelist = [(0,2),(0,3),(1,2),(1,3)]
C4 = [(0,1),(1,2),(2,3),(3,0)]

# paw = 3-pan
paw = [(0,3),(1,2),(1,3),(2,3)]

# diamond = K4 - e = 2-fan
diamond = [(0,2),(0,3),(1,2),(1,3),(2,3)]

# K4 = W3
K4 = [(0,1),(0,2),(0,3),(1,2),(2,3),(1,3)]

graphdict = locals()

graphlist = [twok2,
             claw,
             P4,
             C4,
             paw,
             diamond,
             K4]
