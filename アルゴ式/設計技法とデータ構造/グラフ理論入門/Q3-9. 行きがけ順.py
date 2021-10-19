def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+5))

    N = int(input())
    P = list(map(int, input().split()))

    G = [[] for i in range(N)]
    for A, B in enumerate(P, 1):

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        G[B].append(A)
    
    for i in range(N):
        G[i].sort()
        
    ans=[]
    def dfs(v, p=-1):
        ans.append(v)
        for v_child in G[v]:
            # dfs(v_child) <---> dfs(p) の無限ループを防ぐ
            if v_child == p:
                continue
            # v_child の親をpに格納
            p = v
            dfs(v_child, p)

    dfs(0)
    print(*ans)

if __name__ == '__main__':
    main()