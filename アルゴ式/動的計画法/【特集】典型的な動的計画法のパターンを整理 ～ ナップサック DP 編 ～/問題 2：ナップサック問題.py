def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[-1]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を入力
    dp[0][0] = 0

    # 0, 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M+1):
            # dp[i][j]に移動済みの場合(初期値-1以外が入っている)
            if dp[i][j] != -1:
                # 下に配る
                dp[i+1][j] = max(dp[i][j], dp[i+1][j])
                # 右下に配る
                if j+A[i] <= M:
                    dp[i+1][j+A[i]] = max(dp[i][j]+B[i], dp[i+1][j+A[i]])

    # 右下のマスの値を出力。到達不可の場合は-1
    print(max(dp[-1]))

if __name__ == '__main__':
    main()