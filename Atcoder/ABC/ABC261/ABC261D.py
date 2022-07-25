def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = [0 for i in range(N+1)]

    for _ in range(M):
        c, y = map(int, input().split())
        bonus[c] = y

    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0

    # 処理
    for i in range(1, N+1):
        for j in range(N+1):
            # dp[i][0] はi-1 のコイントスで裏の場合
            # dp[i][j] -> dp[i][0] での値の変化はなし
            # よって dp[i][0] = max(dp[i-1])
            if j == 0:
                dp[i][0] = max(dp[i-1])
            
            # コイントスで表の場合
            else:
                # dp[i-1][j-1] == -1 からの遷移は不可。
                if dp[i-1][j-1] == -1:
                    continue

                # dp[i-1][j-1] -> dp[i][j]への遷移
                # (i-1)回目で表が出たことによる値加算(X[i-1])と
                # 連続でj回表がでたボーナスによる値加算(bonus[j])
                dp[i][j] = dp[i-1][j-1] + bonus[j] + X[i-1]
    
    
    # 答えを出力
    print(max(dp[-1]))


if __name__ == '__main__':
    main()