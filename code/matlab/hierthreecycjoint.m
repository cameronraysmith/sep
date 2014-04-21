%% marginals
% ostensible marginals correspond to probabilities
% of pairwise states s
% [00 01
%  10 11]

% 1--2 marginal
m(:,:,3) = [0.4 0.1;
            0.1 0.4];

% 2--3 marginal
m(:,:,1) = [0.4 0.1;
            0.1 0.4];

% 1--3 marginal
m(:,:,2) = [0.1 0.4;
            0.4 0.1];

% control distribution (x_4)
% uniform over each controlled
% random variable (x_1,x_2,x_3)
ph = [1/3 1/3 1/3];

%% joint distribution
% p(x_1,x_2,x_3,x_4)
A = zeros([3 3 3 3]);

A(1:2,1:2,3,3) = m(:,:,3)*ph(3);
A(3,1:2,1:2,1) = m(:,:,1)*ph(1);
A(1:2,3,1:2,2) = m(:,:,2)*ph(2);

disp('joint distribution p(x_1,x_2,x_3,x_4)')
dims = size(A);

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

fprintf('\n\n\n')

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

fprintf('\n\n\n')

%% conditional distributions

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