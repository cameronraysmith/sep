function [exitflag, X] = sheafsolve (g,a,p)
if nargin < 1
    g = 2;
    a = 2;
    p = 2;
elseif nargin < 2
    a = 2;
    p = 2;
elseif nargin < 3
    p = 2;
elseif nargin == 3
else
    error('wrong number of input arguments');
end

phen = p^g;
L = g*a;
mod = a^g;
modmap = (a*p)^g;
glomap = p^(g*a);

fprintf(['%0.0f \t g \t genetic loci\n',...
         '%0.0f \t a \t distinct alleles available to each locus\n',...
         '%0.0f \t p \t phenotype values\n',...
         '%0.0f \t p^g \t phenotype assignments\n',...
         '%0.0f \t g*a \t possible alleles for all loci\n',...
         '%0.0f \t a^g \t gene regulatory network modules\n',...
         '%0.0f \t (a*p)^g \t modularized genotype-phenotype maps\n',...
         '%0.0f \t p^(g*a) \t global genotype-phenotype maps\n'],...
         g,...
         a,...
         p,...
         phen,...
         L,...
         mod,...
         modmap,...
         glomap);

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

% for i = 1:mod
%     v(i,:) = genprobvect(phen);
% end

v = drchrnd(ones(1,phen),mod);

V = reshape(v',16,1);
V = [V; 1];

%X = G\V %finds solutions with negative values
[X,fval,exitflag,output,lambda]=linprog(ones(glomap,1),[],[],G,V,zeros(glomap,1),ones(glomap,1));

end

