set(0,'defaultaxesfontsize',16);
scrsz = get(0,'ScreenSize');
hf=figure('Visible','on','Position',[0 0 scrsz(3)/3 scrsz(4)/2]);
set(hf,'Color','w');

hold on
for i = 1:length(ind)
    sum(globsecs{i});
    plot(globsecs{i})
    globsecmat(:,i) = globsecs{i};
    locsecmat(:,i) = locsecs{i}(1:end-1);
end
hold off

distmetric = 'euclidean';

cgo1 = clustergram(globsecmat,'Cluster','row',...
                   'RowPDist',distmetric,'ColumnPDist',distmetric,...
                   'Colormap',redbluecmap,'Standardize','none',...
                   'Symmetric',1,'OptimalLeafOrder',1,'Dendrogram',2,...
                   'AnnotColor','k');
set(0,'ShowHiddenHandles','on') 
allhnds = get(0,'Children');
cgfigidx = strmatch('Clustergram',get(allhnds,'Tag'));
cffighnd = allhnds(cgfigidx);
if length(cffighnd)>1
warning('More than one clustergram handle found. Using most recent clustergram') 
cffighnd = cffighnd(1);
end
cgAx = get(cffighnd,'CurrentAxes');
set(cffighnd,'Color','w','Position',[scrsz(3)/2 0 scrsz(3)/3 scrsz(4)]);
set(cgAx,'FontSize',16);
set(0,'showhiddenHandles','off');

hmo1 = HeatMap(globsecmat,...
                   'Colormap',redbluecmap,'Standardize','column',...
                   'Symmetric',1);
set(0,'ShowHiddenHandles','on') 
allhnds = get(0,'Children');
cgfigidx = strmatch('HeatMap',get(allhnds,'Tag'));
cffighnd = allhnds(cgfigidx);
if length(cffighnd)>1
warning('More than one clustergram handle found. Using most recent clustergram') 
cffighnd = cffighnd(1);
end
cgAx = get(cffighnd,'CurrentAxes');
set(cffighnd,'Color','w','Position',[scrsz(3)/2 0 scrsz(3)/3 scrsz(4)]);
set(cgAx,'FontSize',16);
set(0,'showhiddenHandles','off');

cgo2 = clustergram(locsecmat,'Cluster','row',...
                   'RowPDist',distmetric,'ColumnPDist',distmetric,...
                   'Colormap',redbluecmap,'Standardize','none',...
                   'Symmetric',1,'OptimalLeafOrder',1,'Dendrogram',2,...
                   'AnnotColor','k');
set(0,'ShowHiddenHandles','on') 
allhnds = get(0,'Children');
cgfigidx = strmatch('Clustergram',get(allhnds,'Tag'));
cffighnd = allhnds(cgfigidx);
if length(cffighnd)>1
warning('More than one clustergram handle found. Using most recent clustergram') 
cffighnd = cffighnd(1);
end
cgAx = get(cffighnd,'CurrentAxes');
set(cffighnd,'Color','w','Position',[scrsz(3)/2 0 scrsz(3)/3 scrsz(4)]);
set(cgAx,'FontSize',16);
set(0,'showhiddenHandles','off');

hmo2 = HeatMap(locsecmat,...
                   'Colormap',redbluecmap,'Standardize','column',...
                   'Symmetric',1);
set(0,'ShowHiddenHandles','on') 
allhnds = get(0,'Children');
cgfigidx = strmatch('HeatMap',get(allhnds,'Tag'));
cffighnd = allhnds(cgfigidx);
if length(cffighnd)>1
warning('More than one clustergram handle found. Using most recent clustergram') 
cffighnd = cffighnd(1);
end
cgAx = get(cffighnd,'CurrentAxes');
set(cffighnd,'Color','w','Position',[scrsz(3)/2 0 scrsz(3)/3 scrsz(4)]);
set(cgAx,'FontSize',16);
set(0,'showhiddenHandles','off');


HeatMap(reshape(locsecs{1}(1:16),4,4)','Colormap',redbluecmap,'Standardize','none','Symmetric',0);