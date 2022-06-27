def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))
    inf = 10**9

    # 入力を受け取る
    # R行 × C列の迷路
    R, C = map(int, input().split())

    # 迷路を格納
    maze = []
    for r in range(R):
        s = list(input().rstrip())
        maze.append(s)

    # (sy, sx)スタート、(gy, gx)ゴール
    for r, m in enumerate(maze):
        for c, s in enumerate(m):
            if s == "S":
                sy, sx = r, c
                maze[sy][sx] = "."
            
            if s == "G":
                gy, gx = r, c
                maze[gy][gx] = "."


    # R行 × C列の迷路訪問リストを用意
    # dist = [[[0]*C for _ in range(R)] for _ in range(4)]
    dist = [[inf]*C for _ in range(R)]

    que = deque()
    dist[sy][sx] = 0
    # スタート地点をenqueue
    que.append((sy, sx))

    ans = -1
    while len(que) > 0:
        # 現在地(y, x)を取り出す
        y, x = que.popleft()
        # ゴールにたどり着いたら終了
        if (x == gx) and (y == gy):
            ans = dist[y][x]
            break

        # 上下左右の探索
        for dx, dy in dxdy:
            # 範囲内におさまっているか
            if (0 <= x+dx < C) and (0 <= y+dy < R):
                # 未訪問かつ通行可能か
                if dist[y+dy][x+dx] == inf and maze[y+dy][x+dx] == '.':
                    # 移動先のdistを更新
                    dist[y+dy][x+dx] = dist[y][x] + 1
                    # 移動先の座標(y+dy, x+dx)をenque
                    que.append((y+dy, x+dx))

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()