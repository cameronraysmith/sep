loadPackage "GraphicalModels";
loadPackage "FourTiTwo";
d = (2,2,2,2); R = markovRing d
A = getMatrix("C4_bin.mat")
It = toricMarkov(A,R)
flatten degrees It
