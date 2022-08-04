def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    S = input().rstrip()
    C = list(map(int, input().split()))

    INF = 10**9
    # dp[i][j]：i-1 番目までの和が j である括弧列に変えるために必要な最小コスト
    # dp[N][0] が求める答えとなる
    dp = [[INF for _ in range(N+2)] for _ in range(N+1)]

    # 処理

    # dp[0][0] の初期化
    dp[0][0] = 0
    # DP テーブルの更新
    for i in range(N):
        for j in range(N):
            if S[i] == "(":
                # 括弧列の i 文字目が ( の場合
                # そのまま使えば、和 +1 & コスト +0
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])

                # 反転させれば、和 -1 & コスト C[i]
                if j > 0:
                    dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j]+C[i])
            
            elif S[i] == ")":
                # 括弧列の i 文字目が ) の場合
                # そのまま使えば、和 -1 & コスト +0
                if j > 0:
                    dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])

                # 反転させれば、和 +1 & コスト C[i]
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+C[i])

    # 求める答えは最終的な和が 0 である括弧列の最小コスト = dp[N][0]
    ans = dp[N][0]

    # 答えが初期化につかった無限大のままなら、そのような括弧列は存在しない
    if ans >= INF:
        ans = -1

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()