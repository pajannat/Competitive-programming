def main():
    from sys import stdin
    input = stdin.readline

    # 深さ優先探索
    from collections import deque
    INF = 10**9

    # 入力
    # h行 m列の迷路
    h, m = map(int,input().split())

    C = [] # 迷路の文字配列
    for i in range(h):
        C.append(input().rstrip())

    # 各座標への最短距離の配列（INFで初期化）
    D = [[INF] * m for i in range(h)]

    # 4方向の移動ベクトル
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    # スタートからゴールへの最短距離を求める
    def dfs():
        que = deque()
        que.append([sy, sx]) # スタート地点をキューに入れる
        D[sy][sx] = 0 # スタート地点の距離を0とする

        # キューが空になるまで探索
        while len(que) != 0:
            p = que.pop() # 後入れのキューの要素を取り出す
            for i in range(4): # pから4方向に移動 移動後の点は(nx,ny)
                ny = p[0] + dx[i]
                nx = p[1] + dy[i]
                # 移動可能か、訪れたことがあるかの判定
                if 0 <= nx < m and 0 <= ny < h and C[ny][nx] != "." and D[ny][nx] == INF:
                    # 移動可能ならキューに入れて、その点の距離をpからの距離+1で確定する
                    que.append([ny, nx])
                    D[ny][nx] = D[p[0]][p[1]] + 1


    # 深さ優先探索実行
    # 連結成分の数 cnt
    cnt = 0
    for y in range(h):
        for x in range(m):
            sy, sx = y, x
            # 未探索かつ通行可能な場合
            if D[y][x] == INF and C[y][x] == '#':
                cnt += 1
                # 連結成分を探索済みとする
                dfs()

    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()