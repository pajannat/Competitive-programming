def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    # K+1 × D の行列をN+1 面用意する (N × K+1 × D)
    # 配列全体を -1 に初期化しておく
    dp = [ [[-1]*D for _ in range(K+1)] for _ in range(N+1)]

    # dp[0][0][0]に初期値を入力
    dp[0][0][0] = 0

    for n in range(N):
        for k in range(K+1):
            for d in range(D):
                # dp[n][k][d] == -1 の場合はスキップ
                if dp[n][k][d] == -1:
                    continue

                # 次面(n+1)の同座標([k][d])を埋める (A[n] を選ばない場合の遷移)
                dp[n+1][k][d] = max(dp[n+1][k][d], dp[n][k][d])

                # 次面(n+1)の右下方向([k+1][(d+A[n])%D])を埋める (A[n] を選ぶ場合の遷移)
                if k != K:
                    dp[n+1][k+1][(d+A[n])%D] = max(dp[n+1][k+1][(d+A[n])%D], dp[n][k][d]+A[n])


    # 答えを出力
    print(dp[N][K][0])


if __name__ == '__main__':
    main()