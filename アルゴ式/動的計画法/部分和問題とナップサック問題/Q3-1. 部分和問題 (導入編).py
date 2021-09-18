def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*M for _ in range(N)]

    # dp[0][0]に初期値を入力
    dp[0][0] = 1

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        # 1, 2, ..., M-1 列目を順に計算していく
        for j in range(M):
            # 上からくる場合
            if i-1 >= 0:
                if dp[i-1][j] == 1:
                    dp[i][j] = 1
            # 左上からくる場合
            if (i-1 >= 0) and (j-A[i-1] >= 0):
                if dp[i-1][j-A[i-1]] == 1:
                    dp[i][j] = 1

    # sum(dp[N])を出力
    print(sum(dp[-1]))

if __name__ == '__main__':
    main()