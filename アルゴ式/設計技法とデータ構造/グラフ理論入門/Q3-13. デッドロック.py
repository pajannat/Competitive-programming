def main():
    from sys import stdin
    input = stdin.readline


    # トポロジカルソート
    def topo_sort(G):
        """
        トポロジカルソートは、タスク間に依存関係がある場合、
        どんな順番でタスクをこなせば良いかを決めるのに役立つアルゴリズム。
        topo_sort(G)は、タスク間(頂点間)の依存関係G(※有向グラフ)を受け取り、
        依存関係に従ったタスクの消化順 topo を返す。
        """
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

        # 始点となる点をtopoに格納
        for i in range(N):
            if cnt_lis[i] == 0:
                topo.append(i)
        
        for i in topo:
            # 頂点iに到達したので、
            # 頂点j(頂点iに依存している)の依存数を-1する
            for j in G[i]:
                cnt_lis[j] -= 1
                # 頂点jの依存数が0となった場合、頂点jに移動可能
                # topoに頂点jを格納する。
                if cnt_lis[j] == 0:
                    topo.append(j)

        return topo


    # 入力
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        # G[B].append(A)


    # 答えを出力
    if len(topo_sort(G)) == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()