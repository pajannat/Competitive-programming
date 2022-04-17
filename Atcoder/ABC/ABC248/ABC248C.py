def main():
    from sys import stdin
    input = stdin.readline

    MOD = 998244353
    # 入力を受け取る
    N, M, K = map(int, input().split())

    # dp[i列目まで][総和がj]
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1

    ans = 0
    # 処理
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD
    ans = sum(dp[-1]) % MOD
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()