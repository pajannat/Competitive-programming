def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N × N の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(3010) for _ in range(N+1)]

    # dpに初期値を入力
    for i in range(A[0], 3010):
        if i == A[0]:
            dp[0][i] = 1
        elif i <= B[0]:
            dp[0][i] += 1 + dp[0][i-1]
        else:
            dp[0][i] = dp[0][i-1]
    
    # 1, 2, ..., N 行目を順に計算していく
    for i in range(1, N):
        ai = A[i]
        bi = B[i]
        ai_1 = A[i-1]
        bi_1 = B[i-1]
        for j in range(ai, bi+1):
            dp[i][j] += (dp[i][j-1] + dp[i-1][j]) % 998244353
        for k in range(bi+1, 3010):
            dp[i][k] = dp[i][j]

    print(dp[N-1][-1] % 998244353)

if __name__ == '__main__':
    main()