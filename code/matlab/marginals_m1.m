% reset
close all;
clear;

%
N=30000;
K=3;
T=zeros(N,K);
p=0.8;
q=1-p;
s=0.5;
M=p*ones(3,1);
M(3,1)=q;
C=zeros(2,2,3);
for i=1:N/K
    for k=0:K-1
        if rand > s
            if rand < M(mod(k,K)+1,1)
                T(k*N/K+i,mod(k,K)+1)=1;
                T(k*N/K+i,mod(k+1,K)+1)=1;
                T(k*N/K+i,mod(k+2,K)+1)=-1;   
            else
                T(k*N/K+i,mod(k,K)+1)=1;
                T(k*N/K+i,mod(k+1,K)+1)=0;
                T(k*N/K+i,mod(k+2,K)+1)=-1;
            end
        else
            if rand < M(mod(k,K)+1,1)
                T(k*N/K+i,mod(k,K)+1)=0;
                T(k*N/K+i,mod(k+1,K)+1)=0;
                T(k*N/K+i,mod(k+2,K)+1)=-1;
            else
                T(k*N/K+i,mod(k,K)+1)=0;
                T(k*N/K+i,mod(k+1,K)+1)=1;
                T(k*N/K+i,mod(k+2,K)+1)=-1;
            end
        end
    end
end

for k=0:K-1
    C(1,1,mod(k,K)+1)=sum(T(find(T(:,mod(k,K)+1)==-1),mod(k+1,K)+1)==0 & T(find(T(:,mod(k,K)+1)==-1),mod(k+2,K)+1)==0);
    C(1,2,mod(k,K)+1)=sum(T(find(T(:,mod(k,K)+1)==-1),mod(k+1,K)+1)==0 & T(find(T(:,mod(k,K)+1)==-1),mod(k+2,K)+1)==1);
    C(2,1,mod(k,K)+1)=sum(T(find(T(:,mod(k,K)+1)==-1),mod(k+1,K)+1)==1 & T(find(T(:,mod(k,K)+1)==-1),mod(k+2,K)+1)==0);
    C(2,2,mod(k,K)+1)=sum(T(find(T(:,mod(k,K)+1)==-1),mod(k+1,K)+1)==1 & T(find(T(:,mod(k,K)+1)==-1),mod(k+2,K)+1)==1);
end
(K/N)*C
