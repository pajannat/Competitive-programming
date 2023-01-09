def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    dp = [-1]*(N+1)

    # 処理
    # 初期化
    dp[1] = 0
    for i in range(1, N):
        # iマスに到達不可の場合はスキップ
        if dp[i] == -1:
            continue

        # i -> A[i] に移動する場合
        dp[A[i]] = max(dp[i] + 100, dp[A[i]])
        # i -> B[i] に移動する場合
        dp[B[i]] = max(dp[i] + 150, dp[B[i]])

    # 答えを出力
    print(dp[-1])


if __name__ == '__main__':
    main()