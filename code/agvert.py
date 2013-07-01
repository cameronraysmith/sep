"""
generate vertices of no-disturbance and non-contextual polytopes
for arbitrary n-cycle context graphs
"""

import sys
import numpy as np
import itertools

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
    Return a list of bit strings of length n with k 1s
    >>> kbitl(5,4)
    [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    """
    result = []
    for bits in itertools.combinations(range(n), k):
        s = [0] * n
        for bit in bits:
            s[bit] = 1
        result.append(s)
    return result

def binmat(n):
    """
    Return a list of bit strings of length n with all possible
    combinations of 0s and 1s
    >>> binmat(2)
    ['00', '10', '01', '11']
    """
    M = []
    for k in range(0,n+1):
        M.append(kbitl(n,k))
    M = [item for sublist in M for item in sublist]
    return M

def contprod(n):
    """
    >>> contprod(3)
    [[0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 1, 0, 1, 0],
     [1, 1, 1, 1, 1, 1]]
    """
    M = binmat(n)
    N = []
    for r in M:
        for i in range(len(r)):
            ind = (i+1) % (len(r)-1)
            print ind
            r.append(r[i]*r[(i+1) % (len(r)-1)])
        N.append(r)
    return N

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #N = contprod(3)

# if __name__=='__main__':
#     if len(sys.argv) < 2:
#         print "usage: %s m_max max_focal_dim [mode]" % sys.argv[0]
#         sys.exit(1)
#     else:
#         n = int(sys.argv[1])
#         k = int(sys.argv[2])

#     kbits(n,k)




