import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it

# needs debugging
# maybe something in a networkx update broke it
# http://stackoverflow.com/questions/9213797/graphviz-drawing-maximal-cliques


def draw_circle_around_clique(clique,coords):
    dist=0
    temp_dist=0
    center=[0 for i in range(2)]
    color=colors.next()
    for a in clique:
        for b in clique:
            temp_dist=(coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][2])**2
            if temp_dist>dist:
                dist=temp_dist
                for i in range(2):
                    center[i]=(coords[a][i]+coords[b][i])/2
    rad=dist**0.5/2
    cir = plt.Circle((center[0],center[1]),   radius=rad*1.3,fill=False,color=color,hatch=hatches.next())
    plt.gca().add_patch(cir)
    plt.axis('scaled')
    # return color of the circle, to use it as the color for vertices of the cliques
    return color

#def plot_max_cliques(G,cliques):
global colors, hatches
colors=it.cycle('bgrcmyk')# blue, green, red, ...
hatches=it.cycle('/\|-+*')

# create a random graph
G=nx.gnp_random_graph(n=7,p=0.6)
# remember the coordinates of the vertices
coords=nx.spring_layout(G)

# remove "len(clique)>2" if you're interested in maxcliques with 2 edges
cliques=[clique for clique in nx.find_cliques(G) if len(clique)>2]
#cliques=[clique for clique in nx.find_cliques(G)]

#draw the graph
nx.draw(G,pos=coords)
for clique in cliques:
    print "Clique to appear: ",clique
nx.draw_networkx_nodes(G,pos=coords,nodelist=clique,node_color=draw_circle_around_clique(clique,coords))

plt.savefig('maxcliquegraph.pdf')
