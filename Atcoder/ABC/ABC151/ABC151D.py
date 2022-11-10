def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 入力を受け取る
    # R行 × C列の迷路
    R, C = map(int, input().split())
    max_dist = -1

    # 迷路を格納
    maze = []
    for r in range(R):
        s = input().rstrip()
        maze.append(s)

    # R行 × C列の迷路訪問リストを用意
    # dist = [[[0]*C for _ in range(R)] for _ in range(4)]
    def maze_walk(maze, sy, sx):
        dist = [[-1]*C for _ in range(R)]

        que = deque()
        dist[sy][sx] = 0
        # スタート地点をenqueue
        que.append((sy, sx))

        while len(que) > 0:
            # 現在地(y, x)を取り出す
            y, x = que.popleft()

            # 上下左右の探索
            for dx, dy in dxdy:
                # 範囲内におさまっているか
                if (0 <= x+dx < C) and (0 <= y+dy < R):
                    # 未訪問かつ通行可能か
                    if dist[y+dy][x+dx] == -1 and maze[y+dy][x+dx] == '.':
                        # 移動先のdistを更新
                        dist[y+dy][x+dx] = dist[y][x] + 1
                        # 移動先の座標(y+dy, x+dx)をenque
                        que.append((y+dy, x+dx))
        ret = -1
        for d in dist:
            ret = max(ret, max(d))

        return ret
    
    # スタートの位置を全探索
    # BFSはある点を始点としたときの他のすべての点の最短距離を求める。
    # 任意の二点間(スタート、ゴール)を全探索するのではなく、
    # 始点のみ全探索すれば、BFSで全てのゴールを見られる。
    for sy in range(R):
        for sx in range(C):
            # スタートが壁の場合はスキップ
            if maze[sy][sx] == "#":
                continue
            max_dist = max(max_dist, maze_walk(maze, sy, sx))

    # 答えを出力
    print(max_dist)


if __name__ == '__main__':
    main()