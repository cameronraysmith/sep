loadPackage "FourTiTwo";

R = QQ[p000,p001,p010,p011,p100,p101,p110,p111];
A = getMatrix("C3_bin.mat");
It = toricMarkov(A,R)
