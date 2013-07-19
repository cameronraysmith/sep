"""
minineqrep.py
generate a minimal / full-dimensional representation
of the inequalities / facets of the Kolmogorov consistent
polytope and compute its volume
"""
import sys
import numpy as np
import sympy as sp
import subprocess

def redineq(eqfname):
    """
    input: filename containing Kolmogorov Consistency equalities
           for some hypergraph
    output: polrepindeineqs - polymake compatible minimal
                              representation
            poldim - expected dimension of the resulting polytope
    """
    delimiter = ' '

    fhand = open (eqfname , 'r')

    #kceqsf = [ map(int,line.split(delimiter)) for line in fhand ]
    kceqsf = [[int(x) for x in line.split(delimiter)]
                for line in fhand ]
    kceqsf = np.array(kceqsf)
    fhand.close()

    kceqs = np.zeros(shape=np.shape(kceqsf), dtype=np.int)
    kceqs[:, :-1] = kceqsf[:, 1:]
    kceqs[:, -1] = kceqsf[:, 0]

    kceqsref, ind = sp.Matrix(-1*kceqs).rref(simplified=True)
    kceqsrefa = np.squeeze(np.asarray(kceqsref))

    im1 = np.arange(kceqsrefa.shape[1])
    mask1 = np.ones(len(im1), dtype=bool)
    mask1[ind] = False

    indineqs = kceqsrefa[:, im1[mask1]]
    polrepindineqs = np.zeros(shape=np.shape(indineqs), dtype=np.int)
    polrepindineqs[:, 1:] = indineqs[:, :-1]
    polrepindineqs[:, 0] = indineqs[:, -1]
    polrepindineqs = -1*polrepindineqs

    poldim = polrepindineqs.shape[1] - 1

    return polrepindineqs, poldim

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
    eqmat, poldim = redineq(eqfname)
    posmat = posineqgen(poldim)
    minineqs = eqmat.tolist() + posmat.tolist()

    return minineqs

def runpolymakescript(minineqs, representation, polyproperty):
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

    scriptname = "kcscript.pl"
    fname = open(scriptname,'w')
    fname.write(filestring)
    fname.close()
    polyout = subprocess.check_output(["polymake", "--script",
                                               "kcscript.pl"])

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

def minineqrep(argv):
    """
    usage: python minineqrep.py C4.eq VERTICES
    """
    eqfname = str(argv[0])
    polyproperty = str(argv[1])
    minineqs = minineqgen(eqfname)
    polyout = runpolymakescript(minineqs, "INEQUALITIES", polyproperty)

    if polyproperty == "VERTICES":
        boolepolyverts = booleverts(polyout)
        volboole = runpolymakescript(boolepolyverts, "POINTS", "VOLUME")

        volkolmogorov = runpolymakescript(minineqs,
                                            "INEQUALITIES", "VOLUME")
        vrat = convert(volboole) / convert(volkolmogorov)
        #print "%s/%s ~ %0.6f" % (volboole, volkolmogorov, vrat)
        print volboole
        print volkolmogorov
        print vrat

    print "\n" + polyout
    return polyout

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    minineqrep(sys.argv[1:])
