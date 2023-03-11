def main():

    # 入力を受け取る
    H, W = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(H)]
    dp = [[[] for _ in range(W)] for _ in range(H)]

    dp[0][0].append([G[0][0]])
    # 処理
    for i in range(H):
        for j in range(W):
            for dp_ij in dp[i][j]:
                # 右に移動
                if j+1 >= W:
                    pass
                elif G[i][j+1] not in dp_ij:
                    dp[i][j+1].append(dp_ij + [G[i][j+1]])
                # elif G[i][j+1] not in dp[i][j]:
                #     dp[i][j+1] = dp[i][j] + [G[i][j+1]]

                # 下に移動
                if i+1 >= H:
                    pass
                elif G[i+1][j] not in dp_ij:
                    dp[i+1][j].append(dp_ij + [G[i+1][j]])
                # elif G[i+1][j] not in dp[i][j]:
                #     dp[i+1][j] = dp[i][j] + [G[i+1][j]]


    
    # 答えを出力
    print(len(dp[-1][-1]))


if __name__ == "__main__":
    main()