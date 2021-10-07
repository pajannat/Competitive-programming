def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque

    import sys
    import queue
    input = sys.stdin.readline
    sys.setrecursionlimit(int(1E+7))
    dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))

    H, W = map(int, input().split())
    sy, sx, gy, gx = map(int, input().split())

    maze = []
    for _ in range(H):
        s = input().rstrip()
        maze.append(s)

    # R×Cの訪問リストを用意
    visited = [[0]*W for _ in range(H)]

    q = queue.Queue()

    ans = -1
    # スタート地点をenqueue
    q.put((sy, sx, 0))
    while(not q.empty()):
        y, x, d = q.get()
        # ゴールにたどり着いたら終了
        if (x == gx) and (y == gy):
            ans = d
            break
        # 訪問済みの場合は無視する
        if visited[y][x] == 1:
            continue
        else:
            # 訪問フラグを立てる
            visited[y][x] = 1
            # 上下左右の探索
            for dx, dy in dxdy:
                # 範囲内におさまっているか
                if (0 <= x+dx < W) and (0 <= y+dy < H):
                    # 未訪問かつ通行可能か
                    if visited[y+dy][x+dx] == 0 and maze[y+dy][x+dx] == 'W':
                        # 距離を+1してenqueue
                        q.put((y+dy, x+dx, d+1))

    print(ans)

if __name__ == '__main__':
    main()