import itertools
import numpy as np
import networkx as nx
import sympy as sp
import matplotlib.pyplot as plt
#from openopt import MCP

#import drawmaxcliques


# enumerate non-isomorphic graphs
# on 4 vertices
# http://www.roard.com/docs/cookbook/cbsu5.html
# https://oeis.org/A000088/a000088a.gif
# http://www.graphclasses.org/smallgraphs.html#nodes4

# C3
#edgelist = [(0,1),(1,2),(2,3)]

# C4 = K_{2,2}
#edgelist = [(0,2),(0,3),(1,2),(1,3)]
edgelist = [(0,1),(1,2),(2,3),(3,0)]

# diamond = K4 - e = 2-fan
#edgelist = [(0,2),(0,3),(1,2),(1,3),(2,3)]

# paw = 3-pan
#edgelist = [(0,3),(1,2),(1,3),(2,3)]


condindgraph = nx.Graph(edgelist)

# enumerate maximal cliques
# http://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm\
#nx.max_clique(G)
maxcliquesgen = nx.find_cliques(condindgraph)
maxcliques = list(maxcliquesgen)

# plot maximal cliques
#drawmaxcliques.plot_max_cliques(condindgraph,maxcliques)
coords=nx.spring_layout(condindgraph)
nx.draw(condindgraph,pos=coords)
plt.savefig('maxcliquegraph.pdf')

pvallength = 2 # get from user input
numnodes = condindgraph.number_of_nodes() # get from networkx graph

pvals = range(pvallength)
stateindices = itertools.product(pvals, repeat=numnodes)
columns_states = [list(element) for element in stateindices]

cliquevals = []
cliqueids = []
for clique in maxcliques:
    cliquevaliter = itertools.product(pvals, repeat=np.size(clique))
    for cliqueval in cliquevaliter:
        cliquevals.append(list(cliqueval))
        cliqueids.append(clique)

normconds = np.zeros((len(maxcliques),len(cliqueids)),dtype=np.int)
normconds = np.append(normconds, np.ones_like(normconds[:,0])[...,None],1)
for i,maxclique in enumerate(maxcliques):
    for j,cliqueid in enumerate(cliqueids):
        if maxclique==cliqueid:
            normconds[i,j]=1

ssmat = np.zeros((len(cliquevals),
                  len(columns_states)),dtype=int)

for i,(cv,cid) in enumerate(zip(cliquevals,cliqueids)):
    for j,cs in enumerate(columns_states):
        if cv==[cs[k] for k in cid]:
            ssmat[i,j]=1

eqmat = np.asarray(sp.Matrix(ssmat.T).nullspace(simplified=True),dtype=np.int)
eqmat = np.append(eqmat, np.zeros_like(eqmat[:,0])[...,None],1)
eqmat = np.vstack((eqmat, normconds))

# Read eqmat from macaulay file
# fname = '../macaulay/C4_bin.mar'
# with open(fname) as f:
#     next(f)
#     eqmat = np.array([ map(int,line.split()) for line in f ])

kceqsref, ind = sp.Matrix(eqmat).rref(simplified=True)
kceqsrefs = np.squeeze(np.asarray(kceqsref))
kceqsrefa = kceqsrefs[~np.all(kceqsrefs == 0, axis=1)]

im1 = np.arange(kceqsrefa.shape[1])
mask1 = np.ones(len(im1), dtype=bool)
mask1[ind] = False

indineqs = kceqsrefa[:, im1[mask1]]
polrepindineqs = np.zeros(shape=np.shape(indineqs), dtype=np.int)
polrepindineqs[:, 1:] = -1*indineqs[:, :-1]
polrepindineqs[:, 0] = indineqs[:, -1]
#polrepindineqs = polrepindineqs
