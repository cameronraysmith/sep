loadPackage "FourTiTwo";

R = QQ[p11,p12,p13,p21,p22,p23];
A = getMatrix("I2_bin.mat")
toricMarkov(A)
It = toricMarkov(A,R)
