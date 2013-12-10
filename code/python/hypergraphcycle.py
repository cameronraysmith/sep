"""
hypergraphcycle.py

implementation of the Graham reduction method
for hypergraph cycle detection
http://web.cecs.pdx.edu/~maier/TheoryBook/MAIER/C13.pdf
section 13.3.1
"""

from copy import deepcopy
import numpy as np
import hypergraph as hg
import hypergraph.core as hgc

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

def testcycle(edgelist,numverts):
    hh=hgc.Hypergraph(vertices=set(range(numverts)))
    for e in edgelist:
        hh.add_edge(hgc.Edge(e))
    return graham_reduce(hh)


# for g in graphlist:
#     #print testcycle(g)
#     hh=hgc.Hypergraph(vertices=set([0,1,2,3]))
#     for e in g:
#         hh.add_edge(hgc.Edge(e))
#     print graham_reduce(hh)
