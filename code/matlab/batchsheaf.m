clear;
numiter = 1000000;
errthres = 0.01;

G = [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0;
     0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;
     0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0;
     0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1;
     1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0;
     0 1 0 1 0 1 0 1 0 0 0 0 0 0 0 0;
     0 0 0 0 0 0 0 0 1 0 1 0 1 0 1 0;
     0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 1;
     1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0;
     0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0;
     0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0;
     0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1;
     1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0;
     0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0;
     0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0;
     0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1];

 G = [G; 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];

for i=1:numiter
    [ef(i) X{i} V{i}] = sheafsolve(2,2,2);
    if ~isempty(X{i})
       err(:,i) = (V{i} - G*X{i}).^2;
    else
       err(:,i) = zeros(17,1);
    end
       si(i) = sum(X{i});
end

%linear programming in julia
%http://docs.julialang.org/en/latest/stdlib/glpk/

sse = sum(err);
ind = find(sse ~= 0 & sse < errthres);
globsecs = X(ind);
locsecs = V(ind);
