def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())

    C = [list(map(int, input().split())) for _ in range(N)]

    INF = 10000000000
    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[INF]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を設定
    dp[0][0] = 0

    # 0, 1, 2, ..., N 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M):
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + C[i][j]


    # 右下のマスの値を出力。
    print(dp[-1][-1])

if __name__ == '__main__':
    main()