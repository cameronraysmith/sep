close all;
clear;

T = 1000;
S = 100;
avgKLD1 = [];
maxKLD1 = [];

textprogressbar(sprintf('working...\n'));
for R=1:S:T+1
    textprogressbar(R/T*100)
    for k=1:50
        [avgKLD1v(k),maxKLD1v(k)]=hierarchicalthreecycle(R,T,0,0);
    end
    avgKLD1 = [avgKLD1;
               mean(avgKLD1v), std(avgKLD1v)]; 
    maxKLD1 = [maxKLD1;
               mean(maxKLD1v), std(maxKLD1v)];
           
end
textprogressbar(sprintf('\ndone.'));

figure('Color','w');
set(gca,'FontSize',18);
errorbar(1:S:T+1',avgKLD1(:,1),avgKLD1(:,2),'k.','LineWidth',2)

% figure('Color','w');
% set(gca,'FontSize',18);
hold on;
errorbar([1:S:T+1]'+10,maxKLD1(:,1),maxKLD1(:,2),'rx','LineWidth',2)
hold off;
%set(gca,'YLim',[0,2]);