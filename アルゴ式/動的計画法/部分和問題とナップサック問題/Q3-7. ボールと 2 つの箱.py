def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    W = list(map(int, input().split()))
    M = sum(W)

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

    # 箱の重さの差dfを初期化する
    df = 100000000
    for i in range(M+1):
        # dp[-1][i] == 1は箱の重さをiにできることを表す
        # 片方の箱の重さがiのときのdfを計算、更新
        if dp[-1][i] == 1:
            df = min(df, abs(M-2*i))
    
    print(df)

if __name__ == '__main__':
    main()