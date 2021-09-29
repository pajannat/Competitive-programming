def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())
    A = list(map(int, input().split()))

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [0]*(N+1)

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(N):
        dp[i+1] = max(dp[i], dp[i]+A[i])

    # 右下のマスの値を出力。到達不可の場合は-1
    print(dp[N])

if __name__ == '__main__':
    main()