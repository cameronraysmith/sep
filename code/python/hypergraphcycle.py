import hypergraph as hg
import hypergraph.core as hgc
import numpy as np

# acyclic hypergraph
flagpole = [[1,3,4],[2,3]]
hh1=hgc.Hypergraph()

for e in flagpole:
    hh1.add_edge(hgc.Edge(e))

hh1adj=hg.matrix.adjacency_matrix(hh1)
hh1cycflag = False
for n in range(3,len(hh1.vertices)+1):
    if np.trace(np.linalg.matrix_power(hh1adj,n)) != 0.:
        print "cycle of size %d" % n
        hh1cycflag = True


#print hh1
#print "\n"

# for v in hh1.vertices:
#     print ""
#     dfs = hg.search.depth_first_search(hh1,v)
#     for s in dfs:
#         print s

# cyclic hypergraph
basket = [[1,3,4],[1,2],[2,3]]
hh2=hgc.Hypergraph()

for e in basket:
    hh2.add_edge(hgc.Edge(e))

# print hh2
# print "\n"

# for v in hh2.vertices:
#     print ""
#     dfs = hg.search.depth_first_search(hh2,v)
#     for s in dfs:
#         print s

# acyclic graph
chain = [[1,2],[2,3],[3,4]]
hh3=hgc.Hypergraph()

for e in chain:
    hh3.add_edge(hgc.Edge(e))

hh3adj=hg.matrix.adjacency_matrix(hh3)
hh3cycflag = False
for n in range(3,len(hh3.vertices)+1):
    if np.trace(np.linalg.matrix_power(hh3adj,n)) != 0.:
        print "cycle of size %d" % n
        hh3cycflag = True

# acyclic graph
c4 = [[1,2],[2,3],[3,4],[1,4]]
hh4=hgc.Hypergraph()

for e in c4:
    hh4.add_edge(hgc.Edge(e))

hh4adj=hg.matrix.adjacency_matrix(hh4)
hh4cycflag = False
for n in range(3,len(hh4.vertices)+1):
    if np.trace(np.linalg.matrix_power(hh3adj,n)) != 0.:
        print "cycle of size %d" % n
        hh4cycflag = True

