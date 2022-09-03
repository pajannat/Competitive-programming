def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    Tmax = 10**5
    N = int(input())
    TXA = [[0]*(Tmax + 1) for i in range(5)]
    for i in range(N):
        T, X, A = map(int, input().split())
        TXA[X][T] = A

    # dp[x][t]
    dp = [[-1]*(Tmax + 1) for i in range(5)]

    dp[0][0] = 0
    # 処理
    for t in range(1, Tmax + 1):
        for x in range(5):

            dp[x][t] = max(dp[x][t], dp[x][t-1])

            if x-1 >= 0:
                dp[x][t] = max(dp[x][t], dp[x-1][t-1])

            if x+1 <= 4:
                dp[x][t] = max(dp[x][t], dp[x+1][t-1])

            # dp[x][t]に到達可能な場合
            # (時刻tに座標xへ到達可能な場合)
            if dp[x][t] >= 0:
                dp[x][t] += TXA[x][t]


    # 答えを出力
    print(max(dp[i][Tmax] for i in range(5)))


if __name__ == '__main__':
    main()