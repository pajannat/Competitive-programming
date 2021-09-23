def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    # N+1 × A の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*A for _ in range(N+1)]

    # dp[0]に初期値を入力
    dp[0][0] = 1

    for i in range(N):
        for j in range(A):
            # dp[i][j] == 0 の場合はスキップ
            if dp[i][j] == 0:
                continue

            # 真下を埋める
            dp[i+1][j] = 1

            # 右下を埋める
            dp[i+1][(j+X[i])%A] = 1

    if dp[-1][B] == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()