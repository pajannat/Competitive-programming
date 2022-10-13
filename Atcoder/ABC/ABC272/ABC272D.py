def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque

    # 入力を受け取る
    N, M = map(int, input().split())
    dist = [[-1] * N for i in range(N)]
    dij_list = []
    q = deque()

    # 処理
    for di in range(-N+1, N):
        for dj in range(-N+1, N):
            if di**2 + dj**2 == M:
                dij_list.append([di, dj])
    
    def push(i, j, d):
        if (i < 0) or (j < 0) or (i >= N) or (j >= N):
            return
        if (dist[i][j] != -1):
            return
        dist[i][j] = d
        q.append([i, j])
    
    push(0, 0, 0)

    while len(q) > 0:
        que = q.popleft()
        i = que[0]
        j = que[1]
        for dij in dij_list:
            ni = i + dij[0]
            nj = j + dij[1]
            push(ni, nj, dist[i][j]+1)
    
    # 答えを出力
    for dis in dist:
        print(*dis)


if __name__ == '__main__':
    main()