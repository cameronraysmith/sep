from copy import deepcopy
import numpy as np
import hypergraph as hg
import hypergraph.core as hgc
from graphlist4 import graphlist
from graphlist4 import hgraphlist

def remove_ear(G):
    H = deepcopy(G)
    for v in H.vertices:
        if len(H.incident(v))==1:
            edge_containing_ear = H.incident(v).pop()
            non_ear_vertices = set.difference(set(edge_containing_ear),
                                              set([v]))
            if non_ear_vertices:
                edge_lacking_ear = hgc.Edge(non_ear_vertices)
                edges_lacking_ear = deepcopy(H.edges)
                edges_lacking_ear.remove(edge_containing_ear)
                if any([edge_lacking_ear.issubset(e) for e in edges_lacking_ear]):
                    H.remove_vertex(v)
                else:
                    H.remove_edge(edge_containing_ear)
                    H.add_edge(edge_lacking_ear)
            else:
                H.remove_edge(edge_containing_ear)
            break
    return H

def graham_reduce(G):
    progress_flag = True
    cycle_flag = True
    vertex_counter = 1
    hgstack = [G]
    while progress_flag:
        H = hgstack.pop()
        temp=remove_ear(H)
        if temp.edges:
            if temp==H:
                if vertex_counter > len(G.vertices):
                    progress_flag = False
                    cycle_flag = True
            hgstack.append(temp)
        else:
            progress_flag = False
            cycle_flag = False
        vertex_counter += 1
    return cycle_flag

for g in graphlist:
    #print testcycle(g)
    hh=hgc.Hypergraph(vertices=set([0,1,2,3]))
    for e in g:
        hh.add_edge(hgc.Edge(e))
    print graham_reduce(hh)

print ""

for g in hgraphlist:
    #print testcycle(g)
    hh=hgc.Hypergraph(vertices=set([0,1,2,3]))
    for e in g:
        hh.add_edge(hgc.Edge(e))
    print graham_reduce(hh)


# def testcycle(edgelist):
#     hh=hgc.Hypergraph(vertices=set([0,1,2,3]))
#     for e in edgelist:
#         hh.add_edge(hgc.Edge(e))
#     hhlapeig = np.round(hg.matrix.laplacian_eigenvalues(hg.matrix.laplacian_matrix(hh)))
#     #print hhlapeig
#     if hhlapeig[1]==0:
#         return False
#     elif len(np.unique(hhlapeig)) < 4:
#         return True
#     else:
#         return False

# def cycle_detect(G,root=None):
#     gnodes=G.vertices
#     cycles=[]
#     while gnodes:  # loop over connected components
#         if root is None:
#             root=gnodes.pop()
#         stack=[root]
#         pred={root:root}
#         used={root:set()}
#         while stack:  # walk the spanning tree finding cycles
#             z=stack.pop()  # use last-in so cycles easier to find
#             zused=used[z]
#             for nbr in G.neighbors(z):
#                 if nbr not in used:
#                     pred[nbr]=z
#                     stack.append(nbr)
#                     used[nbr]=set([z])
#                 elif nbr == z:        # self loops
#                     cycles.append([z])
#                 elif nbr not in zused:# found a cycle
#                     pn=used[nbr]
#                     cycle=[nbr,z]
#                     p=pred[z]
#                     while p not in pn:
#                         cycle.append(p)
#                         p=pred[p]
#                     cycle.append(p)
#                     cycles.append(cycle)
#                     used[nbr].add(z)
#         gnodes-=set(pred)
#         root=None
#     return cycles


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
