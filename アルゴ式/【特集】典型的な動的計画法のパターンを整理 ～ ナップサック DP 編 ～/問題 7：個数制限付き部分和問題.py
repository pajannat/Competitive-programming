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

    INF = 10000000000
    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[INF]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を設定
    dp[0][0] = 0

    # 0, 1, 2, ..., N 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M+1):
            # A[i]選んで移動した回数をカウントアップ(dp[i+1][j]に保持)
            # 上からもらう
            if dp[i][j] < INF:
                # 上からもらう場合はA[i]選択しない場合のため0を入力
                dp[i+1][j] = 0
            # 左上からもらう
            if (j-A[i] >= 0) and (dp[i][j-A[i]] < INF):
                # 左上(dp[i][j-A[i]])からもらう場合はA[i]選択の1回
                # 既に上からもらっている場合があるので比較して最小値を入力
                dp[i+1][j] = min(dp[i+1][j], 1)
            # 左からもらう
            # A[i]の選択回数(dp[i][j-A[i]])がB[i]未満の場合
            if (j-A[i] >= 0) and (dp[i+1][j-A[i]] < B[i]):
                # 既に上または左上からもらっている場合があるので
                # 比較して最小値を入力
                # 左からもらう場合はdp[i+1][j-A[i]]に選択回数を1加算
                dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-A[i]] + 1)

    # 右下のマスの値を出力。
    if dp[-1][-1] < INF:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()