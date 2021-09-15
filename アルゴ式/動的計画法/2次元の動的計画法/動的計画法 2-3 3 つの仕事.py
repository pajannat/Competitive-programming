def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N = int(input())

    # N × 3 の配列を用意する
    # 配列全体を 0 に初期化しておく
    # 動的計画法の配列を用意
    dp = [[0]*3 for _ in range(N)]
    # 仕事(i,j)を格納する配列を用意
    W_list = [[0]*3 for _ in range(N)]

    # 0, 1, ..., N-1 行目の入力を受け取る
    for i in range(N):
        W_list[i] = list(map(int, input().split()))

    # 0行目の報酬は、仕事の配列の0行目と一致するため格納する
    dp[0] = W_list[0]

    # 1, 2, ..., N-1 行目を順に計算していく
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + W_list[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + W_list[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + W_list[i][2]

    # dp[N-1]の最大値を出力
    print(max(dp[-1]))

if __name__ == '__main__':
    main()