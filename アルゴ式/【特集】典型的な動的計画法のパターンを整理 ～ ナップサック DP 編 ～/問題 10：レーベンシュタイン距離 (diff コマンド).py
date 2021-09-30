def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()
    T = input().rstrip()
    N = len(S)
    M = len(T)

    INF = 10000000000
    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[INF]*(M+1) for _ in range(N+1)]

    # 上と左を埋める
    for i in range(N+1):
        dp[i][0] = i
    for j in range(M+1):
        dp[0][j] = j

    # 0, 1, 2, ..., N 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M):
            if S[i] == T[j]:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j])
            else:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+1)

    # 右下のマスの値を出力。
    print(dp[-1][-1])

if __name__ == '__main__':
    main()