loadPackage "FourTiTwo";
R = QQ[p11,p12,p13,p21,p22,p23];
{* A = getMatrix("I2_bin.mat") *}
A = matrix{{1, 1, 1, 0, 0, 0},{0, 0, 0, 1, 1, 1},{1, 0, 0, 1, 0, 0},{0, 1, 0, 0, 1, 0},{0, 0, 1, 0, 0, 1}}
toricMarkov(A)
It = toricMarkov(A,R)
