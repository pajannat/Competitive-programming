N, X, d = map(int, input().split())
a0 = X
aN_1 = X + (N-1)*d
print((a0+aN_1)*N//2)