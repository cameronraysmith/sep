"""
Compute kernel and cokernel of a linear
transformation T and verify that the
resulting vectors are indeed mapped to
zero
"""

import numpy as np
import sympy as sp

def cokernel(T):
    """
    usage example:
    Tred, TTred, kerT, cokerT = cokernel(T)

    input: linear transformation T
    output: rref of T,
            rref of T transpose,
            rref of the kernel of T,
            rref of the cokernel of T
    """
    Tred = np.asarray(sp.Matrix(T).rref()[0])
    TTred = np.asarray(sp.Matrix(T.T).rref()[0])
    kerT = np.asarray(sp.Matrix(np.asarray(sp.Matrix(T).nullspace())).rref()[0])
    cokerT = np.asarray(sp.Matrix(np.asarray(sp.Matrix(T.T).nullspace())).rref()[0])

    print "T"
    print Tred
    print ""

    print "T transpose"
    print TTred
    print ""

    print "kernel of T"
    print kerT
    print ""

    print "cokernel of T"
    print cokerT
    print ""

    print "T multiplied by the transpose of the kernel of T"
    print "np.dot(Tred,kerT.T)"
    print np.dot(Tred, kerT.T)
    print ""

    print "T transpose multiplied by the transpose of the cokernel of T"
    print "np.dot(TTred,cokerT.T)"
    print np.dot(TTred, cokerT.T)
    print ""

    return (Tred, TTred, kerT, cokerT)

