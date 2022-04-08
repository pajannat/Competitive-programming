def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input()) # 頂点数
    M = N-1 # 辺の数
    adj = [[] for i in range(N+1)]
    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)


    # 方針
    # 木は2部グラフなので、頂点を2色に塗り分けできる
    # グラフを2色に塗り分ける。同色の頂点は隣り合わない。
    # 2色のうち、数が多いほうからN/2頂点出力する

    even_vertex = []
    odd_vertex = []

    # 幅優先探索で頂点1からの距離を計算
    # 距離の偶奇でグラフを２色に塗り分ける
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
        if dist[i]%2 == 0:
            even_vertex.append(i)
        else:
            odd_vertex.append(i)
    
    # 答えを出力
    if len(even_vertex) == 1:
        print(*even_vertex)
    else:
        if len(even_vertex) > len(odd_vertex):
            print(*even_vertex[:N//2])
        else:
            print(*odd_vertex[:N//2])
    
if __name__ == '__main__':
    main()