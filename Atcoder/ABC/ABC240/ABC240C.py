def main():
    from sys import stdin
    input = stdin.readline

    N, X = map(int, input().split())
    A = [None]*N
    B = [None]*N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    # X × X の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(X+1) for _ in range(N+1)]

    # dp[0][0]に初期値を入力
    dp[0][0] = 1

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        for j in range(X):
            if dp[i][j] != 0:
                if j+A[i] <= X:
                    dp[i+1][j+A[i]] += dp[i][j]
                if j+B[i] <= X:
                    dp[i+1][j+B[i]] += dp[i][j]


    # dp[N-1][N-1]を出力
    if dp[-1][-1] != 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()