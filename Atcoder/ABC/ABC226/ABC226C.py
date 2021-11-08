def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(10000000)  # RecursionError対策

    # 入力
    N = int(input())
    lists = []
    for i in range(N):
        lists.append(list(map(int, input().split())))
    

    # 技i 習得に必要な技をG[i]に格納
    G = [[] for i in range(N)]
    for i, lis in enumerate(lists):
        for B in lis[2:]:

            # 頂点 A から頂点 B への辺を張る
            G[i].append(B-1)

            # 無向グラフの場合は次も実施
            # G[B-1].append(i)
    
    # 技 N を習得した時点で、習得しているべき技にflgを立てる
    # flgとして、技i習得にかかる時間を入力する
    flgs = [0] * (N)
    def dfs(lists, G, i):
        if flgs[i] != 0:
            return
        flgs[i] = lists[i][0]

        for j in G[i]:
            dfs(lists, G, j)
    
    dfs(lists, G, N-1)

    # 出力
    print(sum(flgs))

if __name__ == '__main__':
    main()