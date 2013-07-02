"""
generate vertices of no-disturbance and non-contextual polytopes
for arbitrary n-cycle context graphs
"""

import sys
import numpy as np
import itertools
import subprocess

def kbits(n, k):
    """
    Return a list of bit strings of length n with k 1s
    >>> kbits(5,4)
    ['11110', '11101', '11011', '10111', '01111']
    """
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result

def kbitl(n, k):
    """
    Return a list of bit strings of length n with k -1s
    >>> kbitl(3,2)
    [[-1, -1, 1], [-1, 1, -1], [1, -1, -1]]
    """
    result = []
    for bits in itertools.combinations(range(n), k):
        s = [1] * n
        for bit in bits:
            s[bit] = -1
        result.append(s)
    return result

def binmat(n):
    """
    Return a list of bits of length n with all possible
    combinations of -1s and 1s
    >>> binmat(2)
    [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    """
    x = [-1,1]
    M = [list(p) for p in itertools.product(x, repeat=n)]
    return M

def genvertnc(n):
    """
    >>> genvertnc(3)
    [[-1, -1, -1, 1, 1, 1], [-1, -1, 1, 1, -1, -1], [-1, 1, -1, -1, -1, 1], [-1, 1, 1, -1, 1, -1], [1, -1, -1, -1, 1, -1], [1, -1, 1, -1, -1, 1], [1, 1, -1, 1, -1, -1], [1, 1, 1, 1, 1, 1]]
    """
    M = binmat(n)
    N = []
    for r in M:
        l = len(r)
        for i in range(l):
            r.append(r[i]*r[(i+1) % l])
        N.append(r)
    return N

def contextvert(n):
    """
    >>> contextvert(2)
    [[0, 0, -1, 1], [0, 0, 1, -1]]
    >>> contextvert(3)
    [[0, 0, 0, -1, 1, 1], [0, 0, 0, 1, -1, 1], [0, 0, 0, 1, 1, -1]]
    >>> contextvert(4)
    [[0, 0, 0, 0, -1, 1, 1, 1], [0, 0, 0, 0, 1, -1, 1, 1], [0, 0, 0, 0, 1, 1, -1, 1], [0, 0, 0, 0, 1, 1, 1, -1], [0, 0, 0, 0, -1, -1, -1, 1], [0, 0, 0, 0, -1, -1, 1, -1], [0, 0, 0, 0, -1, 1, -1, -1], [0, 0, 0, 0, 1, -1, -1, -1]]
    """
    odds = range(1,n,2)
    M = []
    for k in odds:
        M.append(kbitl(n,k))
    M = [[0]*n+item for sublist in M for item in sublist]
    return M

def genvertnd(n):
    """
    >>> genvertnd(3)
    [[-1, -1, -1, 1, 1, 1], [-1, -1, 1, 1, -1, -1], [-1, 1, -1, -1, -1, 1], [-1, 1, 1, -1, 1, -1], [1, -1, -1, -1, 1, -1], [1, -1, 1, -1, -1, 1], [1, 1, -1, 1, -1, -1], [1, 1, 1, 1, 1, 1], [0, 0, 0, -1, 1, 1], [0, 0, 0, 1, -1, 1], [0, 0, 0, 1, 1, -1]]
    >>> genvertnd(4)
    [[-1, -1, -1, -1, 1, 1, 1, 1], [-1, -1, -1, 1, 1, 1, -1, -1], [-1, -1, 1, -1, 1, -1, -1, 1], [-1, -1, 1, 1, 1, -1, 1, -1], [-1, 1, -1, -1, -1, -1, 1, 1], [-1, 1, -1, 1, -1, -1, -1, -1], [-1, 1, 1, -1, -1, 1, -1, 1], [-1, 1, 1, 1, -1, 1, 1, -1], [1, -1, -1, -1, -1, 1, 1, -1], [1, -1, -1, 1, -1, 1, -1, 1], [1, -1, 1, -1, -1, -1, -1, -1], [1, -1, 1, 1, -1, -1, 1, 1], [1, 1, -1, -1, 1, -1, 1, -1], [1, 1, -1, 1, 1, -1, -1, 1], [1, 1, 1, -1, 1, 1, -1, -1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, -1, 1, 1, 1], [0, 0, 0, 0, 1, -1, 1, 1], [0, 0, 0, 0, 1, 1, -1, 1], [0, 0, 0, 0, 1, 1, 1, -1], [0, 0, 0, 0, -1, -1, -1, 1], [0, 0, 0, 0, -1, -1, 1, -1], [0, 0, 0, 0, -1, 1, -1, -1], [0, 0, 0, 0, 1, -1, -1, -1]]
    """
    L = genvertnc(n)
    M = contextvert(n)
    N = L + M
    return N

def addOnesCol(M):
    """
    >>> addOnesCol(genvertnd(2))
    [[1, -1, -1, 1, 1], [1, -1, 1, -1, -1], [1, 1, -1, -1, -1], [1, 1, 1, 1, 1], [1, 0, 0, -1, 1], [1, 0, 0, 1, -1]]
    """
    N = []
    for r in M:
        r.insert(0, 1)
        N.append(r)
    return N

def writePolymakeScript(n, flag=0):
    if flag == 1:
        M = addOnesCol(genvertnc(n))
    else:
        M = addOnesCol(genvertnd(n))

    f = open('pmscript.pl','w')

    filestring = "$Verbose::credits=0;\nuse application \"polytope\";\nmy $ncpoints=new Matrix<Rational>(%s);\nmy $nc=new Polytope<Rational>(POINTS=>$ncpoints);\nprint $nc->VOLUME;" % str(M)

    f.write(filestring)

def convert(s):
    try:
        return float(s)
    except ValueError:
        num, denom = s.split('/')
        return float(num) / float(denom)

def runPolymake(n):
    writePolymakeScript(n,1)
    vnc = subprocess.check_output(["polymake","--script","pmscript.pl"])
    print vnc
    writePolymakeScript(n,0)
    vnd = subprocess.check_output(["polymake","--script","pmscript.pl"])
    print vnd
    vrat = convert(vnc)/convert(vnd)
    return vrat

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# if __name__=='__main__':
#     if len(sys.argv) < 2:
#         print "usage: %s m_max max_focal_dim [mode]" % sys.argv[0]
#         sys.exit(1)
#     else:
#         n = int(sys.argv[1])
#         k = int(sys.argv[2])

#     kbits(n,k)
