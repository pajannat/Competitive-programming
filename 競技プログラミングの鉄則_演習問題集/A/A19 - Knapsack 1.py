def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, W = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(W + 1) for _ in range(N+1)]


    # 処理
    for i in range(N):
        for j in range(len(dp[i])):
            w_i = WV[i][0]
            v_i = WV[i][1]
            if dp[i][j] != 0:
                # 下に配る
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                # 右下に配る
                if j+w_i < W+1:
                    dp[i+1][j+w_i] = max(dp[i+1][j+w_i], dp[i][j]+v_i)
            # 品物i 1つのみを選ぶ場合
            dp[i+1][w_i] = max(dp[i+1][w_i], v_i)


    # 答えを出力
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
