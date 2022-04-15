def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque

    # 入力を受け取る
    # R行 × C列の迷路
    R, C = map(int, input().split())
    # (sy, sx)スタート、(gy, gx)ゴール
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy, sx = sy - 1, sx - 1
    gy, gx = gy - 1, gx - 1

    # 迷路を格納
    maze = []
    for _ in range(R):
        s = input().rstrip()
        maze.append(s)

    inf = 10**9
    # R行 × C列の迷路訪問リストを用意
    dist = [inf]*(R*C*4)

    # 障害物で通れない場所を探す（距離をマイナスにしておく）
    for r in range(R):
        for c in range(C):
            if maze[r][c] == "#":
                for i in range(4):
                    dist[(C*sy + sx)*4 + i] = -1

    que = deque()
    # スタート地点をenqueue
    for i in range(4):
        que.append((sy, sx, i))
    
    # スタート地点は距離0
    for i in range(4):
        dist[(C*sy + sx)*4 + i] = 0
    
    # x, y の移動方向
    dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while que :
        # 現在地と方向(y, x, now_direct)を取り出す
        y, x, now_direct = que.popleft()

        # 上下左右の探索
        for nex_direct, (dx, dy) in enumerate(dxdy):

            # 範囲外はスキップ
            if not (0 <= x+dx <= C-1 and 0 <= y+dy <= R-1):
                continue
            # 通行不可の場合はスキップ
            if maze[y+dy][x+dx] == '#':
                continue

            # コスト0で移動
            if nex_direct == now_direct:
                if dist[(C*(y+dy)+(x+dx))*4 + nex_direct] > dist[(C*y+x)*4 + now_direct]:
                    dist[(C*(y+dy)+(x+dx))*4 + nex_direct] = dist[(C*y+x)*4 + now_direct]
                    # 更新順を保つために、コスト0移動は前へenque
                    que.appendleft((y+dy, x+dx, nex_direct))
            # コスト1で移動
            else:
                if dist[(C*(y+dy)+(x+dx))*4 + nex_direct] > dist[(C*y+x)*4 + now_direct] + 1:
                    dist[(C*(y+dy)+(x+dx))*4 + nex_direct] = dist[(C*y+x)*4 + now_direct] + 1
                    # 更新順を保つために、コスト1移動は後ろへenque
                    que.append((y+dy, x+dx, nex_direct))

    ans = inf
    for i in range(4):
        if dist[(gy*C + gx)*4 + i] == -1:
            continue
        ans = min(ans, dist[(C*gy+gx)*4 + i])
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()