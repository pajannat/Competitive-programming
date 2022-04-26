def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # DPテーブル
    # dp[a][b]が最小となるように、dp[a][b-1]を選ぶ
    # dp[a][b] (0<=a<=2 ,0<=b<=N-1)
    dp = [[10**9]*N for _ in range(3)]

    # DP初期条件
    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0

    ABC = [A, B, C]

    # 処理
    # i-1列のマスからi列のマスへの移動を考える
    for i in range(1, N):
        # i列のj行のマスへの移動をそれぞれ考える(j=0,1,2)
        # j=0 -> A, j=1 -> B, j=2 -> C
        for j in range(3):
            # マス(j, i)への移動はどのマス(k, i-1)からが最適かを探索(k=0,1,2)
            for k in range(3):
                # (k, i-1) -> (j, i)の遷移にかかるcost
                cost = abs(ABC[j][i]-ABC[k][i-1])
                # より最適なパターンを見つけた場合
                dp[j][i] = min(dp[j][i], dp[k][i-1]+cost)

    # 答えを出力
    print(min(dp[0][-1], dp[1][-1], dp[2][-1]))


if __name__ == '__main__':
    main()