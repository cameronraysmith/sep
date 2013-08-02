#!/bin/sh

#------------------------------
# needs file C4_bin.mod
#------------------------------

# see http://www.4ti2.de/genModel.html
# compute sufficient statistics matrix A
# from simplicial complex (a graph in this case)
# (or a graphical statistical model)
# input: C4_bin.mod
# output: C4_bin.mat
/opt/4ti2/bin/genmodel C4_bin

# see http://www.4ti2.de/markov.html
# compute Markov basis
# input: C4_bin.mat
# output: C4_bin.mar
/opt/4ti2/bin/markov C4_bin

cat C4_bin.mod
cat C4_bin.mat
cat C4_bin.mar
