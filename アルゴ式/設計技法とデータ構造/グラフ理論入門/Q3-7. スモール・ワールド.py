def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque

    # 入力
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        # 頂点Aから頂点Bへの辺を張る
        G[A].append(B)
        # 頂点Bから頂点Aへの辺を張る
        G[B].append(A)

    # 頂点 0 から各頂点 i までの距離をdist[i]に記録
    dist = [-1] * N
    # 頂点 0 から頂点 0 までの距離は 0
    dist[0] = 0

    d = deque()
    d.append(0)

    # dにキューがある限り処理を続ける
    while d:
        # dの左端から一つ取り出す
        v = d.popleft()
        # 頂点 v から到達可能な頂点 i を探索
        for i in G[v]:
            # 頂点 i に到達済みの場合はスキップ
            if dist[i] != -1:
                continue
            # 未到達の場合は、(頂点 0 から)頂点 i までの距離を計算
            # 頂点 0 から移動するごとに+1する
            # 累積値が(頂点 0 から)頂点 i までの距離となる
            dist[i] = dist[v] + 1
            # 頂点 i の先を探索するために、dにキューとしてiを格納
            d.append(i)

    # 答えを出力
    print(max(dist))

if __name__ == '__main__':
    main()