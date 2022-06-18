def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
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
    
    # 処理
    # 連結成分の個数 cnt
    cnt = 0
    # 頂点iを全探索
    for i in range(N):
        # 未訪問の頂点iを発見した場合
        if d[i] == 0:
            cnt += 1
            # 頂点iからDFSして, 連なる成分を発見済みとする
            dfs(i, 0)
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()