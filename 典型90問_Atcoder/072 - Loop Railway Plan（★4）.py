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
        # 訪問済みのマスの場合
        if dist[sh][sw] != -1:
            # 始点に戻ってくるまでに移動3回以上の場合
            if cnt - dist[sh][sw] >= 3:
                return cnt - dist[sh][sw]
            # 始点に戻ってくるまでに移動2回以下の場合
            else:
                return -1
        
        # 打ち切りでない場合の処理

        # バックトラック処理
        # push
        num = -1
        dist[sh][sw] = cnt
        # 再帰処理
        for dh, dw in dxdy:
            h = sh + dh
            w = sw + dw
            # 範囲内かつ通行可能か
            if (0 <= h < H) and (0 <= w < W) and C_list[h][w] == '.':
                num = max(num, dfs(h, w, cnt + 1))
        # pop
        dist[sh][sw] = -1

        return num
    
    ans = -1
    for i in range(H):
        for j in range(W):
            if C_list[i][j] == '.':
                ans = max(ans, dfs(i, j, 0))

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()