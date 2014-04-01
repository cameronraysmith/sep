function [avgKLD1,maxKLD1] = hierarchicalthreecycle(R,N,plotflag,verbflag)

% reset
close all;
%clear;

% number of lower-level samples
% per higher-level sample
%
% (higher-level process is assumed
%  to be slower than the lower-level
%  process, so this should always be
%  greater than or equal to 1)
%
% R = 100;

% number of samples
% N=1000;

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
    if ~mod(i-1,R)
        k = randsample(3,1);
    end
    
    % store history of higher-level states
    z(i)=k;
    
    % sample pair state
    ps = find(mnrnd(1,m(:,:,k)));
    
    % sample triple state
    T(i,k) = -1;
    T(i,e(k,1)) = s(ps,1);
    T(i,e(k,2)) = s(ps,2);
end

% compute and plot pairwise histograms from triple states
KLD1=[];
KLD2=[];

for k = 1:size(T,2)
    if sum(T(:,k)==-1)==0
        continue
    end
    TT = T(T(:,k)==-1,:);
    [q,i,j]=unique(TT,'rows');
    [f,x]=hist(j);
    f = f(f~=0);
    fn = f/sum(f);
    if length(fn)~=4
        continue
    end
    KLD1 = [KLD1 sum(m(:,:,k).*log2(m(:,:,k)./fn'))];
    KLD2 = [KLD2 sum(fn'.*log2(fn'./m(:,:,k)))];
    
    if verbflag
        fprintf('\ntriple state counts for node %d inactive, edge %d--%d\n',k,e(k,1),e(k,2));
        disp([q f']);
    end
    
    if plotflag
        figure('Color','w');
        bar(1:4,fn);
        set(gca,'FontSize',18);
        set(gca,'XTick',1:4);
        title(sprintf('node %d inactive, edge %d--%d',k,e(k,1),e(k,2)));
        xlabel('pairwise state');
        ylabel('probability');
    end
end

if verbflag
    fprintf('\nmean kld(real,empirical)')
    disp(mean(KLD1))
    fprintf('\nmean kld(empirical,real)')
    disp(mean(KLD2))
    fprintf('\nmax kld(real,empirical)')
    disp(max(KLD1))
    fprintf('\nmax kld(empirical,real)')
    disp(max(KLD2))
end

avgKLD1=mean(KLD1);
maxKLD1=max(KLD1);

end
