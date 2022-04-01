def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, L = map(int, input().split())
    dp = [0]*(N+1)

    MOD = 10**9 + 7

    dp[0] = 1

    for i in range(1, N+1):
        dp[i] = (dp[i] + dp[i-1]) % MOD
        if i-L >= 0:
            dp[i] = (dp[i] + dp[i-L]) % MOD
    
    print(dp[-1])

if __name__ == '__main__':
    main()