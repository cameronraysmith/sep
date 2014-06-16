"""
modelselect.py

1. given a list of probabilities
2. determine which graphical model(s) contain it
"""
import itrecipes
import numpy as np
import itertools

def subsetsize(ss):
    if not map(len,ss):
        return 0
    else:
        return max(map(len,ss))

def removesubsets(ss):
    fs = frozenset([m for i,m in enumerate(ss)
                    if not any(m < n for n in ss)])
    return fs

def genhypergraphs(vertices):
    #vertices=[1,2,3]
    #baseset = [frozenset([i]) for i in range(vertices)]
    baseset = vertices
    ps = itrecipes.powerset(baseset)
    ps.next() # burn the empty list
    psl = map(frozenset,ps)
    hg = itrecipes.powerset(psl)
    hgs = map(frozenset,hg)
    hgf = map(removesubsets,hgs)
    hgf = list(set(hgf))
    return hgf

def ssfromgraph(edgelist=[(0,1),(1,2),(2,3),(3,0)],
                graphname="graph", pvallist=None,
                printlevel=1):
    """
    input: edgelist = the list of edges of a graph
           pvallength = the number of discrete values each node can take
    output: polrepindineqs - polymake compatible minimal
                              representation
            poldim - expected dimension of the resulting polytope
    """
    maxcliques = map(list, edgelist)

    numnodes = len(set([item for sublist in maxcliques for item in sublist]))

    if pvallist is None:
        pvallist = 2*np.ones(numnodes,dtype=np.int)

    stateindices = itertools.product(*map(range,pvallist))
    columns_states = [list(element) for element in stateindices]

    cliquevals = []
    cliqueids = []
    for clique in maxcliques:
        cliquevaliter = itertools.product(*map(range,
                                         [pvallist[i] for i in clique]))
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

    # Read ssmat from macaulay file
    # fname = '../macaulay/C4_bin.mat'
    # with open(fname) as f:
    #     next(f)
    #     ssmat = np.array([ map(int,line.split()) for line in f ])

    if printlevel:
        print "States"
        print columns_states
        print""

        print "Edge IDs"
        print cliqueids
        print""

        print "KC / sufficient statistics matrix"
        print ssmat
        print ""

    return ssmat
