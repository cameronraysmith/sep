import sys
import numpy as np
import sympy as sp
import subprocess

def redineq(eqfname):
    delimiter = ' '

    fhand = open ( eqfname , 'r')
    l1 = [ map(int,line.split(delimiter)) for line in fhand ]
    l1 = np.array(l1)
    fhand.close()

    l2 = np.zeros(shape=np.shape(l1), dtype=np.int)
    l2[:, :-1] = l1[:, 1:]
    l2[:, -1] = l1[:, 0]

    ref, ind = sp.Matrix(-1*l2).rref(simplified=True)
    refa = np.squeeze(np.asarray(ref))

    im1 = np.arange(refa.shape[1])
    mask1 = np.ones(len(im1), dtype=bool)
    mask1[ind] = False

    indineqs = refa[:, im1[mask1]]
    polrepindineqs = np.zeros(shape=np.shape(indineqs), dtype=np.int)
    polrepindineqs[:,1:] = indineqs[:,:-1]
    polrepindineqs[:,0] = indineqs[:, -1]
    polrepindineqs = -1*polrepindineqs
    return polrepindineqs

def posineqgen(n):
    z = np.zeros(shape=(n,n+1), dtype=np.int)
    z[:,1:] = np.identity(n)
    return z

def minineqgen(eqfname,n):
    eqmat = redineq(eqfname)
    posmat = posineqgen(n)
    ineqs = eqmat.tolist() + posmat.tolist()
    #print sp.Matrix(ineqs)
    return ineqs

def writePolymakeScript(M):

    filestring = str("$Verbose::credits=0;\nuse application "
                     "\"polytope\";\nmy $ndineqs=new "
                     "Matrix<Rational>(%s);\nmy $nd=new "
                     "Polytope<Rational>(INEQUALITIES=>$ndineqs);\nprint "
                     "$nd->VERTICES;" % str(M))

    return filestring

def minineqrep(argv):
    """
    usage: python rrefmat.py C4.eq 8
    """
    eqfname = str(argv[0])
    n = int(argv[1])
    M = minineqgen(eqfname,n)
    filestring = writePolymakeScript(M)
    scriptname = "kcscript.pl"
    f = open(scriptname,'w')
    f.write(filestring)
    vnd = subprocess.check_output(["polymake","--script","kcscript.pl"])
    print vnd
    return vnd

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    minineqrep(sys.argv[1:])
