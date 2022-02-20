def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(1000000)  # RecursionError対策

    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]
    A_list = []
    B_list = []
    for i in range(1, M+1):
        A, B = map(int, input().split())
        A_list.append(A)
        B_list.append(B)
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)
    color = [0] * (N+1) # 0->無 1->赤 2->青

    def dfs(v):
        for next in adj[v]: # 頂点vに隣接するv1,v2,...を探索
            if color[next] == 0: # 未訪問なら
                color[next] = 3 - color[v]
                dfs(next)
    
    for i in range(1, N+1):
        if color[i] == 0:
            color[i] = 1
            dfs(i)
    
    # 二部グラフかどうかを判別
    flg = True
    for i in range(M):
        if color[A_list[i]] == color[B_list[i]]:
            flg = False

    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")
 
if __name__ == '__main__':
    main()