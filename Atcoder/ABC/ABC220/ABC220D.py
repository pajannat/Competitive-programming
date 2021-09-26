def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353

    # N-1 × 10 の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*10 for _ in range(N)]

    # dpの0行目に初期値を入力
    for i in range(10):
        if i == A[0]:
            dp[0][i] = 1

    # 0, 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N-1):
        # 0, 1, 2, ..., 9 列目を順に計算していく
        for j in range(10):
            if dp[i][j] != 0:
                dp[i][j] = dp[i][j] % mod
                # A[0]は使用済み。A[1]から使用する。
                # よって、iのときにA[i+1]を使う。
                # 操作F
                dp[i+1][(j+A[i+1])%10] += dp[i][j]
                # 操作G
                dp[i+1][(j*A[i+1])%10] += dp[i][j]

    for i in dp[-1]:
        print(i % mod)

if __name__ == '__main__':
    main()