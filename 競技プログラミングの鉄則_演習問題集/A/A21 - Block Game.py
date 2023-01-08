def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    P = [0]
    A = [0]
    for _ in range(N):
        p, a = map(int, input().split())
        P.append(p)
        A.append(a)
    
    ans = 0

    dp = [[0]*(N+1) for _ in range(N+2)]

    # 処理
    # dp[L][R] -> L番目からR番目までブロックが残っているときのscoreの最大値
    # 初期値
    dp[1][N] = 0
    for i in range(1, N+1):
        for j in range(1, N+1)[::-1]:
            # ブロックをすべて取り除いた場合はスキップ
            if i > j:
                continue

            # 上から配られる場合(左からブロックを取り除く)
            # スコアが得られるとき
            if i <= P[i-1] <= j:
                ue = dp[i-1][j] + A[i-1]
            # スコアが得られないとき
            else:
                ue = dp[i-1][j]

            # 右から配られる場合(右からブロックを取り除く)
            # 右端のときは migi = 0
            if j+1 >= N+1:
                migi = 0
            # スコアが得られるとき
            elif i <= P[j+1] <= j:
                migi = dp[i][j+1] + A[j+1]
            # スコアが得られないとき
            else:
                migi = dp[i][j+1]
            
            dp[i][j] = max(ue, migi)

    # スコアの最大値を探す
    for i in range(len(dp)):
        ans = max(ans, max(dp[i]))

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()