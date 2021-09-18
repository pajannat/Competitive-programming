def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    W = list(map(int, input().split()))

    # N+1 × M+1 の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(M+1) for _ in range(N+1)]

    # dp[0]に初期値を入力
    dp[0][0] = 1

    for i in range(N):
        for j in range(M+1):
            # dp[i][j] == 0 の場合はスキップ
            if dp[i][j] == 0:
                continue

            # 真下を埋める
            dp[i+1][j] = 1

            # 右下を埋める
            if j+W[i] <= M:
                dp[i+1][j+W[i]] = 1

    if dp[N][M] == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()