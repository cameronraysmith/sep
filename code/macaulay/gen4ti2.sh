#!/bin/sh

#------------------------------
# needs file such as C4_bin.mod
#------------------------------

# see http://www.4ti2.de/genModel.html
# compute sufficient statistics matrix A
# from simplicial complex (a graph in this case)
# (or a graphical statistical model)
# input: C4_bin.mod
# output: C4_bin.mat
/opt/4ti2/bin/genmodel $1

# see http://www.4ti2.de/markov.html
# compute Markov basis
# input: C4_bin.mat
# output: C4_bin.mar
/opt/4ti2/bin/markov $1

cat $1.mod
cat $1.mat
cat $1.mar
