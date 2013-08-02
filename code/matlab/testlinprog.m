G = [3 2 -1;
     2 -2 4;
    -1 1/2 -1];
V = [1; -2; 0];
 
[X,fval,exitflag,output,lambda]=linprog(ones(3,1),[],[],G,V,[0,-5,-5],[2,5,5])