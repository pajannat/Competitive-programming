def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    # 各マスの情報を取得
    field = [list(map(int, input().split())) for _ in range(N)]

    # N × N の配列を用意する
    # 配列全体を 10000000 に初期化しておく
    INF = 10000000
    dp = [[INF]*N for _ in range(N)]

    # dp[0][N-1]に初期値を入力
    dp[0][N-1] = field[0][N-1]

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        # N-1, N-2, ..., 1 列目を順に計算していく
        for j in reversed(range(N)):
            # 上または右からくる場合
            if (i != 0) and (j != N-1):
                dp[i][j] = field[i][j] + min(dp[i-1][j], dp[i][j+1])
            # 上だけからくる場合
            elif i != 0:
                dp[i][j] = field[i][j] + dp[i-1][j]
            # 右だけからくる場合
            elif j != N-1:
                dp[i][j] = field[i][j] + dp[i][j+1]

    # dp[N-1][0]を出力
    print(dp[N-1][0])

if __name__ == '__main__':
    main()