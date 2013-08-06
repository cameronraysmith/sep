loadPackage "FourTiTwo";
loadPackage "StatePolytope";

R = QQ[p0000,p0001,p0010,p0011,
       p0100,p0101,p0110,p0111,
       p1000,p1001,p1010,p1011,
       p1100,p1101,p1110,p1111]
gens R
A = getMatrix("C4_bin.mat")
M = toricMarkov(A)
It = toricMarkov(A,R)
flatten degrees It

statePolytope(It)
--time(G,L) = gfan It;
--G/toString/print;
--L/toString/print;
