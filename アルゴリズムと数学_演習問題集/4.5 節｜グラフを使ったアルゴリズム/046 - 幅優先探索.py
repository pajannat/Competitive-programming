def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    
    # 入力を受け取る
    # R行 × C列の迷路
    R, C = map(int,input().split())
    # (sy, sx)スタート、(gy, gx)ゴール
    sy, sx = map(int,input().split())
    gy, gx = map(int,input().split())

    # 迷路を格納
    maze = []
    for r in range(R):
        s = input().rstrip()
        maze.append(s)

    adj = [[] for i in range(C*R)]
    # 横方向の辺 [(i, j) - (i, j+1)] をグラフに追加
    for i in range(R):
        for j in range(C-1):
            if maze[i][j] == "." and maze[i][j+1] == ".":
                idx1 = i*C + j
                idx2 = i*C + j+1
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)
    
    # 縦方向の辺 [(i, j) - (i+1, j)] をグラフに追加
    for i in range(R-1):
        for j in range(C):
            if maze[i][j] == "." and maze[i+1][j] == ".":
                idx1 = i*C + j
                idx2 = (i+1)*C + j
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)

    start = (sy-1)*C + (sx-1)
    goal = (gy-1)*C + (gx-1)

    dist = [-1]*(C*R)
    dist[start] = 0

    d = deque()
    d.append(start)

    while d:
        v = d.popleft()
        for i in adj[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    print(dist[goal])
 
if __name__ == '__main__':
    main()