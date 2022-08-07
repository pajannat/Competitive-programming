def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(100000)  # RecursionError対策

    N, M, s, t = map(int, input().split())
    adj = [[] for i in range(N)]
    visited = [0 for _ in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        # adj[B].append(A)

    def dfs(v, t, path):
        visited[v] = 1
        new_path = path + [v]

        if v == t:
            ans = new_path
            print(len(new_path))
            print(*new_path)

        for next in adj[v]: # 頂点vに隣接するv1,v2,...を探索
            if visited[next] == 0: # 未発見なら
                dfs(next, t, new_path)
    
    # 頂点sから探索開始
    dfs(s,t,[])
    
    # 答えを出力
    # if visited[s]==1 and visited[t]==1:
    #     print('Yes')
    # else:
    #     print('No')


if __name__ == '__main__':
    main()