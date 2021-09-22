def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    W = list(map(int, input().split()))

    # N × M の配列を用意する
    # 配列全体を INF に初期化しておく
    INF = 10000000000
    dp = [[INF]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を入力
    dp[0][0] = 0

    # 0, 1, ..., N-1 行目を順に計算していく
    for i in range(N):
        # 0, 1, ..., M 列目を順に計算していく
        for j in range(M+1):
            # dp[i][j]に移動済みの場合(初期値INF以外が入っている)
            if dp[i][j] != INF:
                # 下に配る
                dp[i+1][j] = min(dp[i][j], dp[i+1][j])
                # 右下に配る(最終列の番号len(dp[0])-1を超えない場合)
                if j+W[i] <= len(dp[0])-1:
                    dp[i+1][j+W[i]] = min(dp[i][j]+1, dp[i+1][j+W[i]])

    # 右下のマスの値を出力。到達不可の場合は-1
    if dp[-1][-1] == INF:
        print(-1)
    else:
        print(dp[-1][-1])

if __name__ == '__main__':
    main()
