def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [10**10]*N

    dp[0] = 0
    for i in range(N):
        for j in range(i-M, i):
            dp[i] = min(dp[i], dp[j]+A[i]*(i-j))

    print(dp[N-1])
if __name__ == '__main__':
    main()