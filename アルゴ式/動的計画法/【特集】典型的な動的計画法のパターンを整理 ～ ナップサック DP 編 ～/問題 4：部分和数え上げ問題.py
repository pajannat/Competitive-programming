def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を設定
    dp[0][0] = 1

    mod = 1000

    # 0, 1, 2, ..., N 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M+1):
            # 上からもらう
            dp[i+1][j] = (dp[i+1][j]+dp[i][j]) % mod
            # 左上からもらう
            if j-A[i] >= 0:
                dp[i+1][j] = (dp[i+1][j]+dp[i][j-A[i]]) % mod

    # 右下のマスの値を出力。
    print(dp[-1][-1])

if __name__ == '__main__':
    main()