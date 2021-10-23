def main():
    from sys import stdin
    input = stdin.readline


    # トポロジカルソート(あり得るソート結果のうち、辞書順最小の結果を返却する版)
    def topo_sortmin(G):
        """
        トポロジカルソートは、タスク間に依存関係がある場合、
        どんな順番でタスクをこなせば良いかを決めるのに役立つアルゴリズム。
        topo_sortmin(G)は、タスク間(頂点間)の依存関係G(※有向グラフ)を受け取り、
        依存関係に従ったタスクの消化順 topo を返す。
        ※あり得るソート結果のうち、辞書順最小の結果を返す。
        """
        import heapq

        # Gの頂点数 N
        N = len(G)

        # トポロジカルソートの結果の格納先
        topo = []
        
        # 頂点iに向かう矢印(辺)の本数。依存数。
        cnt_lis = [0] * N

        # 各頂点の依存数をカウント
        for i in range(N):
            for j in G[i]:
                cnt_lis[j] += 1

        d = []
        heapq.heapify(d)
        # 始点となる点をdに格納
        for i in range(N):
            if cnt_lis[i] == 0:
                heapq.heappush(d, i)
        
        while d:
            i = heapq.heappop(d)
            topo.append(i)
            # 頂点iに到達したので、
            # 頂点j(頂点iに依存している)の依存数を-1する
            for j in G[i]:
                cnt_lis[j] -= 1
                # 頂点jの依存数が0となった場合、頂点jに移動可能
                if cnt_lis[j] == 0:
                    heapq.heappush(d, j)

        return topo


    # 入力
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A-1].append(B-1)

        # 無向グラフの場合は次も実施
        # G[B].append(A)
    
    ans = []
    for num in topo_sortmin(G):
        ans.append(num+1)

    # 答えを出力
    if len(ans) == N:
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()