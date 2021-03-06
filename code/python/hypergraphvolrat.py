"""
hypergraphvolrat.py

given a hypergraph generate a minimal / full-dimensional representation
of the inequalities definitive of (H-rep) the locally consistent
polytope of probability distributions and compute the ratio of its
volume to that of the corresponding globally consistent polytope
"""
import sys
import numpy as np
import sympy as sp
import subprocess
import re
import itertools
from fractions import Fraction

from graphlist4 import graphdict

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

def posineqgen(poldim):
    """
    output: polymake compatibile positivity inequalities
    """
    posineq = np.zeros(shape=(poldim, poldim+1), dtype=np.int)
    posineq[:, 1:] = np.identity(poldim)
    return posineq

def minineqgen(eqfname):
    """
    output: minineqs - combine the Kolmogorov Consistency inequalities
                       with positivity inequalities
    """
    eqmat, poldim = kcfromgraph(graphdict[eqfname],eqfname)
    posmat = posineqgen(poldim)
    minineqs = eqmat.tolist() + posmat.tolist()

    return minineqs, poldim

def runpolymakescript(minineqs, representation, polyproperty, eqfname='graph'):
    """
    intermediate: filestring - polymake script with full-dimensional / minimal
                         H-representation of the Kolmogorov Consistent
                         polytope
    output: polyout - output of polymake for given minineqs and
                      polyproperty
    """
    filestring = str("$Verbose::credits=0;\nuse application "
                     "\"polytope\";\nmy $ndineqs=new "
                     "Matrix<Rational>(%s);\nmy $nd=new "
                     "Polytope<Rational>(%s=>$ndineqs);\nprint "
                     "$nd->%s;" %
                     (str(minineqs), representation, polyproperty))

    scriptname = eqfname + "kcscript.pl"
    fname = open(scriptname,'w')
    fname.write(filestring)
    fname.close()
    polyout = subprocess.check_output(["polymake", "--script",
                                               scriptname])

    return polyout

def booleverts(polyvertices):
    """
    remove rational vertices
    """
    def filtrat(line):
        """
        filter lines with '/'s indicating rational numbers
        """
        if "/" not in line:
            vert = [int(x) for x in line.split(' ')]
            return vert
        else:
            return

    filtverts = [filtrat(line)
                             for line in polyvertices.split('\n')[:-1]]
    filtverts = [l for l in filtverts if l is not None]
    return filtverts

def convert(srat):
    """
    convert rational number string to float
    """
    try:
        return float(srat)
    except ValueError:
        num, denom = srat.split('/')
        return float(num) / float(denom)

def approxvol(minineqs,eqfname,error_threshold=0.2):
    minineqstr = re.sub(r'], ',r'],\n',str(minineqs))

    centroid = list(0.125*np.ones(np.shape(minineqs)[1]-1))
    filestring = str("addpath('volconvbod');\n"
                     "aa=%s;\n"
                     "bb = [aa(:,2:end) aa(:,1)];\n"
                     "bb(:,1:end-1)=-1*bb(:,1:end-1);\n"
                     "intpoint = %s';\n"
                     "Volume(bb,[],%s,intpoint)" %
                     (minineqstr, centroid, error_threshold))
    scriptname = eqfname + "Vol"
    fname = open(scriptname + ".m",'w')
    fname.write(filestring)
    fname.close()

    #matlab -nodesktop -nojvm -nosplash -r "run polymakeVol; exit;"
    matprocout = subprocess.check_output(["matlab", "-nodesktop",
                                      "-nojvm", "-nosplash",
                                      "-logfile", scriptname + ".out",
                                      "-r", scriptname + "; exit;"])
    fname = open(scriptname + ".out")
    matout = fname.read()
    fname.close()
    vollist = re.findall(r'(?<=Final Volume: ).*(?=,)',matout)
    vol = float(vollist[0])
    return vol

def minineqrep(argv):
    """
    usage: python minineqrep.py C4 VERTICES
    """
    eqfname = str(argv[0])
    polyproperty = str(argv[1])

    print "Name of graph: \n%s\n" % eqfname

    minineqs, dim = minineqgen(eqfname)
    polyout = runpolymakescript(minineqs, "INEQUALITIES",
                                polyproperty, eqfname)

    #poutbmatrix = bmatrix(polyout)

    if polyproperty == "VERTICES":
        boolepolyverts = booleverts(polyout)
        volboole = runpolymakescript(boolepolyverts,
                            "POINTS", "VOLUME", eqfname)

        volkolmogorov = runpolymakescript(minineqs,
                                        "INEQUALITIES", "VOLUME", eqfname)
        vrat = convert(volboole) / convert(volkolmogorov)
        #print "%s/%s ~ %0.6f" % (volboole, volkolmogorov, vrat)
        print "Volume of Boole polytope"
        print volboole
        print ""

        print "Volume of Kolmogorov polytope"
        print volkolmogorov
        print ""

        print "Volume ratio Boole:Kolmogorov"
        print vrat
        print ""

    print "Vertices of Kolmogorov polytope\n" + polyout
    return vrat, dim

if __name__ == "__main__":
    minineqrep(sys.argv[1:])
