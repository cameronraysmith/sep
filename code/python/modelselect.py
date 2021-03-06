"""
modelselect.py

1. given a list of probabilities
2. determine which graphical model(s) contain it
"""
import itrecipes
import numpy as np
import itertools
import re
import subprocess

import hypergraphlattice as hgl

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

    return ssmat, columns_states

def multiple_replace(dict, text):
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

#http://code.activestate.com/recipes/577124-approximately-equal/
def float_approx_equal(x, y, tol=1e-18, rel=1e-7):
    if tol is rel is None:
        raise TypeError('cannot specify both absolute and relative errors are None')
    tests = []
    if tol is not None: tests.append(tol)
    if rel is not None: tests.append(rel*abs(x))
    assert tests
    return abs(x - y) <= max(tests)

def toric_markov(edgelist=[(0,1),(1,2),(2,3),(3,0)]):
    ssmat, states = ssfromgraph(edgelist,printlevel=0)

    pvarlist = ['p'+''.join(map(str,i)) for i in states]
    pvarstring = re.sub(r'\'',r'',str(pvarlist))

    nparraytoM2matrixdict = {
        '[' : '{',
        ']' : '}',
        '\n': '',
        ' ' : ','
    }

    ssmatstring = multiple_replace(nparraytoM2matrixdict,str(ssmat))

    M2script = str("loadPackage \"FourTiTwo\";\n"
                    "R = QQ%s;\n"
                    "A = matrix%s\n"
                    "toricMarkov(A)\n"
                    "It = toricMarkov(A,R);\n"
                    "toString(It)\n" %
                    (pvarstring, ssmatstring))
    p=subprocess.Popen("M2", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    m2output = p.communicate(input=M2script)[0]
    m2outputpython = re.sub('\^','**',re.sub('\s*','',m2output))
    numvars = str(len(states[0]))
    # polyregex = str(r'((\s?([-\+]\s)?(p[0-1]{%s}\*)+(p[0-1]{%s}))+)' % (numvars, numvars))
    polyregex = str(r'(([-\+]?(p[0-1]{%s}(\*\*\d)?\*)+(p[0-1]{%s}(\*\*\d)?))+)' % (numvars, numvars))
    polyregexfind = re.findall(polyregex,m2outputpython)
    quadrics = [p[0] for p in polyregexfind]

    return quadrics, pvarlist

def check_model(edgelist=[(0,1),(1,2),(2,3),(3,0)],probabilities=[0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625],showvals=False):
    quadrics, pvarlist = toric_markov(edgelist)
    uniformprob = str(1.0/len(pvarlist))
    modelcheckargs = str('='+uniformprob+',').join(pvarlist)+'='+uniformprob

    if showvals:
        quadriceqs = ",".join(quadrics)
        modelcheckfunstr = str("def modelcheck(%s):\n"
                           "\treturn [%s"
                           "]" %
                           (modelcheckargs,quadriceqs))
    else:
        quadriceqs = ",0,1e-2) & float_approx_equal(".join(quadrics)
        modelcheckfunstr = str("def modelcheck(%s):\n"
                           "\treturn float_approx_equal(%s"
                           ",0,1e-2)" %
                           (modelcheckargs,quadriceqs))
    exec(modelcheckfunstr)
    return modelcheck(*probabilities)

def check_models(probabilities=[0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625],numverts=4):
    vertlist = range(numverts)
    lattice = hgl.genhypergraphlattice(vertlist);
    hypergraphlist = hgl.filternonfulllist(lattice.Uelements,numverts)
    # potentialmodellist = []
    quadricvaluelist = []
    for graph in hypergraphlist:
        # if check_model(graph,probabilities):
            # potentialmodellist.append(graph)
        print graph
        quadricvaluelist.append((graph,check_model(graph,probabilities,True)))
    # return potentialmodellist, quadricvaluelist
    return quadricvaluelist

def find_consistent_graphs(quadricvaluelist):
    consistentgraphs = []
    for graphcheck in quadricvaluelist:
        if all(map(lambda x: float_approx_equal(x,0,tol=1e-3),graphcheck[1])):
            consistentgraphs.append(graphcheck[0])
    return consistentgraphs

def check_random_probs(numverts,numdists):
    dists = np.random.dirichlet(tuple([1]*2**numverts),numdists)
    results = []
    for dist in dists:
        print dist
        qvl = check_models(dist,numverts)
        cgs = find_consistent_graphs(qvl)
        results.append((dist,cgs))
    return results

