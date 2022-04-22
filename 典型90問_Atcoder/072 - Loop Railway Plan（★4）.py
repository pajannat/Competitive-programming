def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    C_list = [list(input()) for _ in range(H)]

    dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dist = [[-1]*W for _ in range(H)]

    # 処理
    # スタート地点からバックトラックする再帰関数
    def dfs(sh, sw, cnt):
        # 打ち切り条件
        # 訪問済みのマスに到達した場合に打ち切り
        # 始点と終点が一致していない場合もあるが、
        # 始点と終点が一致している場合が距離最大となり採用されるため問題なし
        if dist[sh][sw] != -1:
            # 訪問済みマスに到達までに移動3回以上の場合
            if cnt - dist[sh][sw] >= 3:
                return cnt - dist[sh][sw]
            # 訪問済みマスに到達までに移動2回以下の場合
            else:
                return -1
        
        # 打ち切りでない場合の処理

        # バックトラック処理
        # push
        kyori = -1
        dist[sh][sw] = cnt
        # 処理
        # 周りを探索。最大となるループの大きさを求める。
        for dh, dw in dxdy:
            h = sh + dh
            w = sw + dw
            # 範囲内かつ通行可能か
            if (0 <= h < H) and (0 <= w < W) and C_list[h][w] == '.':
                kyori = max(kyori, dfs(h, w, cnt + 1))
        # pop
        dist[sh][sw] = -1

        # 入力(sh, sw, cnt)に対する探索結果 dfs(sh, sw, cnt)を返す
        return kyori
    
    ans = -1
    for i in range(H):
        for j in range(W):
            if C_list[i][j] == '.':
                ans = max(ans, dfs(i, j, 0))

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()