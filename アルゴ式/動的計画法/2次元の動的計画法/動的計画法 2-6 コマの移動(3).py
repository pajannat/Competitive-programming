def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    # 各マスの情報を取得
    field = [list(map(int, input().split())) for _ in range(N)]

    # N × N の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*N for _ in range(N)]

    # dp[0][0]に初期値を入力
    dp[0][0] = field[0][0]

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        # 1, 2, ..., N-1 列目を順に計算していく
        for j in range(N):
            # 上または左からくる場合
            if (i != 0) and (j != 0):
                dp[i][j] += field[i][j] + max(dp[i-1][j], dp[i][j-1])
            # 上からくる場合
            elif i != 0:
                dp[i][j] += field[i][j] + dp[i-1][j]
            # 左からくる場合
            elif j != 0:
                dp[i][j] += field[i][j] + dp[i][j-1]

    # dp[N-1][N-1]を出力
    print(dp[-1][-1])

if __name__ == '__main__':
    main()