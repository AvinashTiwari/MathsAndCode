v2 = [3 -2];
v3 = [4; -3; 2];

v3'

figure(1), clf
subplot(211)
plot([0 v2(1)], [0 v2(2)], 'linew',2)
axis square
axis([-4 4 -4 4])
hold on
plot(get(gca , 'xlim'), [0,0], 'k--')
plot([0,0], get(gca , 'ylim'), 'k--')
xlabel('X_1 dimenson')
ylabel('X_2 dimenson')



