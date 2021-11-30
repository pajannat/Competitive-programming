def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    G = [[] for i in range(N)]

    for i in range(1, N):
        # 頂点 A から頂点 B への辺を張る
        G[i].append(A[i-1])

        # 無向グラフの場合は次も実施
        # G[A[i-1]].append(i)
    
    cnt = 0
    tmp = X
    for i in range(N):
        if tmp == 0:
            break

        cnt += 1

        tmp = G[tmp][0]

    print(cnt)

if __name__ == '__main__':
    main()