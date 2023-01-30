def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[-1] * (N) for _ in range(N)]
    # 初期化
    for i in range(N):
        dp[-1][i] = A[i]

    # 処理
    # 0 <= i <= N-2 を, N-2 から降順に繰り返し
    for i in range(N-2, -1, -1):
        # 偶数段のとき
        # 先手(太郎)の選択
        if i % 2 == 0:
            for j in range(i+1):
                # 左下と右下のうち大きいほうの数値
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        # 奇数段のとき
        # 後手(次郎)の選択
        else:
            for j in range(i+1):
                # 左下と右下のうち小さいほうの数値
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

    # 答えを出力
    print(dp[0][0])


if __name__ == '__main__':
    main()