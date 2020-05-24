v1 = [1 2 3 4 5 ];
v2 = [0 -4 -3 6 5];

dp = sum(v1.*v2);
dp = dot(v1,v2);
dp = v1*v2;

dp = 0

for i=1; length(v1)
  dp = dp + v1(i) * v2(i);
endfor
