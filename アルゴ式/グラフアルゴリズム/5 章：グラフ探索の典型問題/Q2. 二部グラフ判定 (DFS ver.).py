def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(100000)  # RecursionError対策

    N, M = map(int, input().split())
    adj = [[] for i in range(N)]
    visited = [-1 for _ in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)

    def dfs(v, kyori):
        kyori += 1
        visited[v] = kyori
        for next in adj[v]: # 頂点vに隣接するv1,v2,...を探索
            # 未訪問の場合
            if visited[next] == -1: # 未発見なら
                dfs(next, kyori)
    
    # 頂点0から探索開始
    for i in range(N):
        # 未訪問の頂点(連結成分)を探索
        if visited[i] == -1:
            dfs(i, 0)

    # 二部グラフの判定
    flg = True
    for i, a in enumerate(adj):
        for j in a:
            # 辺の両端点が同色であればFalse
            if visited[i]%2 == visited[j]%2:
                flg = False
    
    # 答えを出力
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()