def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split()) 
    G = [[] for i in range(N)]
    ans = [[] for i in range(N+1)]
    flg = [0]*N

    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        G[B].append(A)
    
    ans[0].append(0)
    flg[0] = 1
    for i in range(len(ans)-1):
        for x in ans[i]:
            for n in G[x]:
                if flg[n] == 1:
                    continue
                else:
                    ans[i+1].append(n)
                    flg[n] = 1
    
    for a in ans:
        a.sort()
        print(*a)

if __name__ == '__main__':
    main()