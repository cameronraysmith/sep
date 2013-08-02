loadPackage "GraphicalModels";
loadPackage "FourTiTwo";
d = (2,2,2,2);
R = markovRing d
gens R
A = getMatrix("C4_bin.mat")
M = toricMarkov(A)
Ib = toBinomial(M,R)
flatten degrees Ib
It = toricMarkov(A,R)
flatten degrees It
