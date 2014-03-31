% reset
close all;
clear;

% number of samples
N=300;

% number of variables
K=3;

% container for samples
T=zeros(N,K);

% edges
e = [2 3;
     1 3;
     1 2];

% pairwise states
s = [0 0;
     0 1;
     1 0;
     1 1];

% marginals correspond to probabilities
% of pairwise states s
% [00 01
%  10 11]

% 2--3 marginal
m(:,:,1) = [0.4;
            0.1; 
            0.1;
            0.4];

% 1--3 marginal 
m(:,:,2) = [0.1;
            0.4; 
            0.4;
            0.1];

% 1--2 marginal         
m(:,:,3) = [0.4;
            0.1; 
            0.1;
            0.4];
    
for i = 1:N
    % sample inactive variable index
    k = randsample(3,1);
    
    % sample pair state
    ps = find(mnrnd(1,m(:,:,k)));
    
    % sample triple state
    T(i,k) = -1;
    T(i,e(k,1)) = s(ps,1);
    T(i,e(k,2)) = s(ps,2);    
end

% compute and plot pairwise histograms from triple states
for k = 1:size(T,2)
    TT = T(T(:,k)==-1,:);
    [q,i,j]=unique(TT,'rows');
    [f,x]=hist(j);
    fprintf('\ntriple state counts for node %d inactive, edge %d--%d\n',k,e(k,1),e(k,2));
    disp([q f(f~=0)']);
    figure('Color','w');
    bar(x,f/sum(f));
    set(gca,'FontSize',18);
    set(gca,'XTick',1:4);
    title(sprintf('node %d inactive, edge %d--%d',k,e(k,1),e(k,2)));
    xlabel('pairwise state');
    ylabel('probability');
end