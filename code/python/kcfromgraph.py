import itertools
import numpy as np
#import networkx as nx
import sympy as sp
import matplotlib.pyplot as plt
import ipdb

#import drawmaxcliques

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if isinstance(a, np.ndarray):
        if len(a.shape) > 2:
            raise ValueError('bmatrix can at most display two dimensions')
        lines = str(a).replace('[', '').replace(']', '').splitlines()
    elif isinstance(a, str):
        lines = a.splitlines()
    else:
        raise ValueError('wrong input type')
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def kcfromgraph(edgelist=[(0,1),(1,2),(2,3),(3,0)],
                graphname="graph", pvallist=None,
                printlevel=1):
    """
    input: edgelist = the list of edges of a graph
           pvallength = the number of discrete values each node can take
    output: polrepindineqs - polymake compatible minimal
                              representation
            poldim - expected dimension of the resulting polytope
    """
    #condindgraph = nx.Graph(edgelist)

    # enumerate maximal cliques
    # http://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm\
    #nx.max_clique(G)
    #maxcliquesgen = nx.find_cliques(condindgraph)
    #maxcliques = list(maxcliquesgen)
    # assume edges are maximal cliques

    #maxcliques = map(list, condindgraph.edges())
    maxcliques = map(list, edgelist)

    # plot maximal cliques
    # drawmaxcliques.plot_max_cliques(condindgraph,maxcliques)

    #coords=nx.spring_layout(condindgraph)
    #nx.draw(condindgraph,pos=coords)
    #plt.savefig(graphname + 'graph.pdf')

    #numnodes = condindgraph.number_of_nodes() # get from networkx graph
    numnodes = len(set([item for sublist in maxcliques for item in sublist]))

    if pvallist is None:
        pvallist = 2*np.ones(numnodes,dtype=np.int)

    #pvals = range(pvallength)
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

    eqmat = np.asarray(sp.Matrix(ssmat.T).nullspace(simplified=True),dtype=np.int)
    eqmat = np.append(eqmat, np.zeros_like(eqmat[:,0])[...,None],1)
    eqmat = np.vstack((eqmat, normconds))

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

    poldim = polrepindineqs.shape[1] - 1

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

        print "Full set of equalities (non-homogeneous rhs for normalization)"
        print eqmat
        print ""

        print "Reduced equalities (non-homogeneous rhs)"
        print kceqsrefa
        print ""

        print "Polymake reduced inequalities (homogeneous rhs in first column)"
        print "Each line describes one linear inequality."
        print "The encoding is as follows: "
        print "(a_0,a_1,...,a_d) is the inequality a_0 + a_1 x_1 + ... + a_d x_d >= 0."
        print polrepindineqs
        print ""

        print "dimension %d\n" % poldim

    return polrepindineqs, poldim


