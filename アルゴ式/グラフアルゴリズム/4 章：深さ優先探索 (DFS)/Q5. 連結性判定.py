def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(100000)  # RecursionError対策

    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]

    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)
    d = [0] * (N+1) # 発見時刻
    f = [0] * (N+1) # 完了時刻


    def dfs(v, t):
        t+=1 # 発見したらインクリメント
        d[v] = t
        for next in adj[v]: # 頂点vに隣接するv1,v2,...を探索
            if d[next] == 0: # 未発見なら
                t = dfs(next, t)
        t+=1 # 完了してもインクリメント
        f[v] = t
        return t
    
    # 頂点0から深さ優先探索
    dfs(0, 0)

    # 到達した頂点の数
    cnt = 0
    for num in f:
        if num != 0:
            cnt += 1
    
    if cnt == N:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()