%% pairwise distributions associated to three-cycle graph

%
% probabilities of pairwise binary states
% correspond to ostensible marginals
% of p(x_1,x_2,x_3) for global state
% X = (x_1,x_2,x_3) in {0,1}^3
%
% [p(00) p(01)
%  p(10) p(11)]
%

% 1--2 marginal
m(:,:,3) = [0.4 0.1;
            0.1 0.4];

% 2--3 marginal
m(:,:,1) = [0.4 0.1;
            0.1 0.4];

% 1--3 marginal
m(:,:,2) = [0.1 0.4;
            0.4 0.1];

[x,y,z]=meshgrid(1:2,1:2,1:3);
scatter3(x(:),y(:),z(:),90,m(:),'filled');
view(gca,60,60);
%slice(x,y,z,m,[1 2],[1 2],[1 2 3]);
%isosurface(x,y,z,m,0.1)
%isosurface(x,y,z,m,0.4)

%% joint distribution

%
% p(x_1,x_2,x_3,x_4)
% for global state
% X = (x_1,x_2,x_3,x_4) in {1,2,3}^4
%

% distribution of control
% random variable x_4
% over each controlled
% random variable (x_1,x_2,x_3)
ph = [1/3 1/3 1/3];

dims = [3 3 3 3];
A = zeros(dims);

A( 3 , 1:2, 1:2, 1) = m(:,:,1)*ph(1);
A(1:2,  3,  1:2, 2) = m(:,:,2)*ph(2);
A(1:2, 1:2,  3 , 3) = m(:,:,3)*ph(3);

fprintf('\njoint distribution p(x_1,x_2,x_3,x_4)\n')
fprintf('------------------------------\n')

fprintf('x1x2x3x4 \t probability (including zeros)\n\n')
for i = 1:dims(1)
    for j = 1:dims(2)
        for k = 1:dims(3)
            for l = 1:dims(4)
                fprintf('  %d%d%d%d \t\t %f\n',i,j,k,l,A(i,j,k,l))
            end
        end
    end
end

fprintf(['------------------------------\n\n'...
         '------------------------------\n'])

fprintf('x1x2x3x4 \t probability (non-zeros only)\n\n')
for i = 1:dims(1)
    for j = 1:dims(2)
        for k = 1:dims(3)
            for l = 1:dims(4)
                if A(i,j,k,l)~=0
                    fprintf('  %d%d%d%d \t\t %f\n',i,j,k,l,A(i,j,k,l))
                end
            end
        end
    end
end

fprintf('------------------------------\n\n\n')

%% conditional distributions

disp('conditional distributions')
fprintf('------------------------------\n')

% 1--2 conditioned on x_3=3, x_4=3
% p(x_1,x_2 | x_3=3, x_4=3) = p(x_1,x_2,x_3=3,x_4=3)/p(x_3=3,x_4=3)
p12 = A(:,:,3,3)./sum(sum(A(:,:,3,3)));
disp('1--2 conditioned on x_3=3, x_4=3')
disp(p12)

% 2--3 conditioned on x_1=3, x_4=1
% p(x_2,x_3 | x_1=3, x_4=1) = p(x_1=3,x_2,x_3,x_4=1)/p(x_1=3,x_4=1)
p23 = reshape(A(3,:,:,1),3,3)./sum(sum(A(3,:,:,1)));
disp('2--3 conditioned on x_1=3, x_4=1')
disp(p23)

% 1--3 conditioned on x_2=3, x_4=2
% p(x_1,x_3 | x_2=3, x_4=2) = p(x_1,x_2=3,x_3,x_4=2)/p(x_2=3,x_4=2)
p13 = reshape(A(:,3,:,2),3,3)./sum(sum(A(:,3,:,2)));
disp('1--3 conditioned on x_2=3, x_4=2')
disp(p13)

fprintf('------------------------------\n')