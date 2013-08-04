import itertools
import numpy as np
import networkx as nx
import sympy as sp
#from openopt import MCP


# enumerate non-isomorphic graphs
# on 4 vertices
# http://www.roard.com/docs/cookbook/cbsu5.html
# https://oeis.org/A000088/a000088a.gif
edgelist = [(0,2),(0,3),(1,2),(1,3)]
#edgelist = [(0,2),(0,3),(1,2),(1,3),(2,3)]
#edgelist = [(0,3),(1,2),(1,3),(2,3)]
#edgelist = [(0,1),(1,2),(2,3)]

condindgraph = nx.Graph(edgelist)

# enumerate maximal cliques
# http://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm\
#nx.max_clique(G)
maxcliquesgen = nx.find_cliques(condindgraph)
maxcliques = list(maxcliquesgen)

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

eqmat = np.zeros((len(cliquevals),
                  len(columns_states)),dtype=int)

for i,(cv,cid) in enumerate(zip(cliquevals,cliqueids)):
    for j,cs in enumerate(columns_states):
        if cv==[cs[k] for k in cid]:
            eqmat[i,j]=1

#eqmat = np.append(eqmat, np.zeros_like(eqmat[:,0])[...,None],1)
#eqmat = np.vstack((eqmat, np.ones_like(eqmat[0,:])))
#normvect = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1]
#eqmat = np.vstack((eqmat, normvect))

kceqsref, ind = sp.Matrix(eqmat).rref(simplified=True)
kceqsrefs = np.squeeze(np.asarray(kceqsref))
kceqsrefa = kceqsrefs[~np.all(kceqsrefs == 0, axis=1)]

im1 = np.arange(kceqsrefa.shape[1])
mask1 = np.ones(len(im1), dtype=bool)
mask1[ind] = False

indineqs = kceqsrefa[:, im1[mask1]
]polrepindineqs = np.zeros(shape=np.shape(indineqs), dtype=np.int)
polrepindineqs[:, 1:] = indineqs[:, :-1]
polrepindineqs[:, 0] = indineqs[:, -1]
#polrepindineqs = -1*polrepindineqs
