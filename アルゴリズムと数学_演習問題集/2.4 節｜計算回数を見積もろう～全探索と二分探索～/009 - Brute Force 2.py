def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(M+1) for _ in range(N)]

    # dp[0]に初期値を入力
    dp[0][0] = 1
    if A[0] <= M:
        dp[0][A[0]] = 1

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N-1):
        # 1, 2, ..., M-1 列目を順に計算していく
        for j in range(M+1):
            if (N-1) - i >= 1:
                if dp[i][j] == 1:
                    # 下に配る
                    dp[i+1][j] = 1
                    # 右下に配る
                    if j+A[i+1] <= M:
                        dp[i+1][j+A[i+1]] = 1

    # 答えを出力
    if dp[-1][-1] == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()