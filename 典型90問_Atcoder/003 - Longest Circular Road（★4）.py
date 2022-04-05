def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    M = N - 1
    adj = [[] for i in range(N+1)]
    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)

    # 処理: 木の直径を求める。
    # 頂点を一つ選び、そこからもっとも離れている頂点を求める。これが木の片端になる。
    # この片端からもっとも離れている頂点までの距離を求める。
    # これが木の直径となる。(木の端から端)

    from collections import deque
    dist_from1 = [-1] * (N+1)
    dist_from1[1] = 0

    d = deque()
    d.append(1)

    # 幅優先探索で頂点1から各頂点への最短距離を計算
    while d:
        v = d.popleft()
        for i in adj[v]:
            if dist_from1[i] != -1:
                continue
            dist_from1[i] = dist_from1[v] + 1
            d.append(i)

    # 頂点1から最も離れている頂点を次の頂点(next_vertex)とする
    max_dist_from1 = max(dist_from1)
    next_vertex = dist_from1.index(max_dist_from1)
    d.append(next_vertex)

    dist_from_next_vertex = [-1] * (N+1)
    dist_from_next_vertex[next_vertex] = 0

    # 幅優先探索で頂点"next_vertex"から各頂点への最短距離を計算
    while d:
        v = d.popleft()
        for i in adj[v]:
            if dist_from_next_vertex[i] != -1:
                continue
            dist_from_next_vertex[i] = dist_from_next_vertex[v] + 1
            d.append(i)
    
    # 頂点"next_vertex"から最も離れている頂点までの距離を計算
    # これが木の直径となる
    max_dist_from_next_vertex = max(dist_from_next_vertex)

    # 答えを出力
    print(max_dist_from_next_vertex + 1)

if __name__ == '__main__':
    main()