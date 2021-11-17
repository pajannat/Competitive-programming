N, X, r = map(int, input().split())
print(X*(r**N - 1)%10**9)