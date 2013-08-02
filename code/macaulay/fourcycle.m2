loadPackage "GraphicalModels";

--G = graph{{1,3},{1,4},{2,3},{2,4}};
G = graph{{1,2},{1,4},{3,2},{3,4}};
d = (2,2,2,2); R = markovRing d
gens R
s1 = localMarkov G
compactMatrixForm=false;
markovMatrices(R,s1)
I1 = conditionalIndependenceIdeal(R,s1)
flatten degrees I1

s2 = pairMarkov G
compactMatrixForm=false;
markovMatrices(R,s2)
I2 = conditionalIndependenceIdeal(R,s2)
flatten degrees I2

s3 = globalMarkov G
compactMatrixForm=false;
markovMatrices(R,s3)
I3 = conditionalIndependenceIdeal(R,s3)
flatten degrees I3

I1 == I2
I2 == I3
I1 == I3
