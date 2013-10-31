import hypergraph as hg
import hypergraph.core as hgc
import numpy as np
from graphlist4 import graphlist
from graphlist4 import hgraphlist

def testcycle(edgelist):
    hh=hgc.Hypergraph(vertices=set([0,1,2,3]))
    for e in edgelist:
        hh.add_edge(hgc.Edge(e))
    hhlapeig = np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh)))
    print hhlapeig
    if hhlapeig[1]==0:
        return False
    elif len(np.unique(hhlapeig)) < 4:
        return True
    else:
        return False

for g in graphlist:
    print testcycle(g)

for g in hgraphlist:
    print testcycle(g)


# # acyclic hypergraph
# flagpole = [[1,3,4],[2,3]]
# hh1=hgc.Hypergraph()

# for e in flagpole:
#     hh1.add_edge(hgc.Edge(e))

# hh1adj=hg.matrix.adjacency_matrix(hh1)
# hh1cycflag = False
# for n in range(2,len(hh1.vertices)+1):
#     if np.trace(np.linalg.matrix_power(hh1adj,n)) != 0.:
#         print "cycle of size %d" % n
#         hh1cycflag = True

# print hh1cycflag

# hh1leig= np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh1)))

# # cyclic hypergraph
# basket = [[1,3,4],[1,2],[2,3]]
# hh2=hgc.Hypergraph()

# for e in basket:
#     hh2.add_edge(hgc.Edge(e))

# hh2adj=hg.matrix.adjacency_matrix(hh2)
# hh2cycflag = False
# for n in range(2,len(hh1.vertices)+1):
#     if np.trace(np.linalg.matrix_power(hh2adj,n)) != 0.:
#         print "cycle of size %d" % n
#         hh2cycflag = True

# print hh2cycflag

# hh2leig= np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh2)))

# # acyclic graph
# chain = [[1,2],[2,3],[3,4]]
# hh3=hgc.Hypergraph()

# for e in chain:
#     hh3.add_edge(hgc.Edge(e))

# hh3adj=hg.matrix.adjacency_matrix(hh3)
# hh3cycflag = False
# for n in range(2,len(hh3.vertices)+1):
#     if np.trace(np.linalg.matrix_power(hh3adj,n)) != 0.:
#         print "cycle of size %d" % n
#         hh3cycflag = True

# print hh3cycflag

# hh3leig= np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh3)))

# # cyclic graph
# c4 = [[1,2],[2,3],[3,4],[1,4]]
# hh4=hgc.Hypergraph()

# for e in c4:
#     hh4.add_edge(hgc.Edge(e))

# hh4adj=hg.matrix.adjacency_matrix(hh4)
# hh4cycflag = False
# for n in range(2,len(hh4.vertices)+1):
#     if np.trace(np.linalg.matrix_power(hh4adj,n)) != 0.:
#         print "cycle of size %d" % n
#         hh4cycflag = True

# print hh4cycflag

# hh4leig= np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh4)))
