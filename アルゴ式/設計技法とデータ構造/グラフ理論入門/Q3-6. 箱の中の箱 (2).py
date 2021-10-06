def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    G = [[] for _ in range(N)]

    for i in range(N-1):
        G[A[i]].append(i+1)
    
    dist = [-1] * N
    dist[0] = 0

    d = deque()
    d.append(0)

    while d:
        v = d.popleft()
        for i in G[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    for i in range(1, N):
        print(dist[i])

if __name__ == '__main__':
    main()