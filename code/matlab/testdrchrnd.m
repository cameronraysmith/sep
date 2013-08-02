set(0,'defaultaxesfontsize',16);
scrsz = get(0,'ScreenSize');
hf=figure('Visible','on','Position',[0 0 scrsz(3)/3 scrsz(4)/2]);
set(hf,'Color','w');

b = drchrnd(ones(1,2),1000);
subplot(1,2,1)
plot(b(:,1),b(:,2),'ko');

a = drchrnd(ones(1,3),1000);
subplot(1,2,2)
plot3(a(:,1),a(:,2),a(:,3),'ko');
view([45 45]);