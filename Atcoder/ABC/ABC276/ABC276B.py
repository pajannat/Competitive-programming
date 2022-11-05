def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A-1].append(B)

        # 無向グラフの場合は次も実施
        G[B-1].append(A)

    # 処理
    for i in range(N):
        G[i].sort()
    
    # 答えを出力
    for i in range(N):
        print(len(G[i]), *G[i])


if __name__ == '__main__':
    main()