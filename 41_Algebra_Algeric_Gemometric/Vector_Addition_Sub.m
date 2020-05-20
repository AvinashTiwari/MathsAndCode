v1 = [2 -1]
v2 = [2, 4]
v3 = v1 + v2

figure(2), clf

plot([0 v1(1)], [0 v1(2)], 'b', 'linew',2)
hold on
plot([0 v2(1)] + v1(1), [0 v2(2)] + v1(2), 'r', 'linew',2)
hold on
plot([0 v3(1)], [0 v3(2)], 'k', 'linew',2)
legend({'v1'; 'v2'; 'v1+v2'})

