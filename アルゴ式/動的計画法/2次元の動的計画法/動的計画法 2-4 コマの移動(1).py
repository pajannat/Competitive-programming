def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())

    # N × N の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*N for _ in range(N)]

    # dp[0][0]に初期値を入力
    dp[0][0] = 1

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        for j in range(N):
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]

    # dp[N-1][N-1]を出力
    print(dp[-1][-1])

if __name__ == '__main__':
    main()