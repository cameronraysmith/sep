function r = drchrnd(a,n)
% see http://www.mathworks.com/matlabcentral/newsreader/view_thread/65818
p = length(a);
r = gamrnd(repmat(a,n,1),1,n,p);
r = r ./ repmat(sum(r,2),1,p);
end