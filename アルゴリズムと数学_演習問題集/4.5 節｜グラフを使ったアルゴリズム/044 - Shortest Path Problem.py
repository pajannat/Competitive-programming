def main():
    from sys import stdin
    input = stdin.readline

    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]
    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)

    from collections import deque
    dist = [-1] * (N+1)
    dist[1] = 0

    d = deque()
    d.append(1)

    while d:
        v = d.popleft()
        for i in adj[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    for i in range(1, N+1):
        print(dist[i])

if __name__ == '__main__':
    main()