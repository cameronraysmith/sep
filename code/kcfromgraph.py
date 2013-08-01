import itertools
import numpy as np
import networkx as nx
#from openopt import MCP

edgelist = [(0,2),(0,3),(1,2),(1,3)]
edgelist = [(0,2),(0,3),(1,2),(1,3),(2,3)]
edgelist = [(0,3),(1,2),(1,3),(2,3)]

condindgraph = nx.Graph(edgelist)
#nx.max_clique(G)

#maxcliqueobj = MCP(condindgraph)
#maxcliques = maxcliqueobj.solve('glpk')
#print(maxcliques.ff, maxcliques.solution)

#http://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm
maxcliquesgen = nx.find_cliques(condindgraph)
maxcliques = list(maxcliquesgen)
print maxcliques

pvallength = 2 # get from user input
numnodes = condindgraph.number_of_nodes() # get from networkx graph

pvals = range(pvallength)

stateindices = itertools.product(pvals,repeat=numnodes)

states = [list(element) for element in stateindices]

print [states[5][i] for i in maxcliques[1]]

