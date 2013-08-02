# coding: utf-8
from scipy.linalg import hadamard
from numpy.linalg import det
from numpy.linalg import inv
import sys

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def hadet(n):
   a = hadamard(n)
   da = det(a)
   ina = inv(a)
   return da, a, ina

if __name__== "main":
   hadet(sys.argv[1:])
