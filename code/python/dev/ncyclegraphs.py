import networkx as nx
import matplotlib.pyplot as plt

def gencycgraph(n):

    condindgraph = nx.cycle_graph(n)

    coords = nx.spring_layout(condindgraph)
    nx.draw(condindgraph, pos=coords)
    plt.savefig('C' + str(n) + 'cycgraph.pdf')
    plt.close()
    return condindgraph

nsforgraph = range(3,7)

graphlist = [gencycgraph(n) for n in nsforgraph]

graphnames = ['C'+str(n) for n in nsforgraph]
graphdict = dict(zip(graphnames, graphlist))
