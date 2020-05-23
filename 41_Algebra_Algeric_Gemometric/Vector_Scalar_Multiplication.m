v1 = [3 -1];
l = 2.3;
figure(3), clf
plot([0,v1(1)], [0,v(2)], 'b', 'linew',2)
hold on
plot([0,v1(1)]*l, [0,v(2)]*l, 'r', 'linew',4)
legend({'v1';'v2'})





