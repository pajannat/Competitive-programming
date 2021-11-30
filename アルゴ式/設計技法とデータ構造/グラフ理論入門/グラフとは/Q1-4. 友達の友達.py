def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M, X = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        G[B].append(A)

    # X(アルル)の友達の友達をresultに格納
    # 同じ人を重複して格納する場合があるのでsetで管理
    result = set()

    # X(アルル)の友達iについて探索
    for i in G[X]:
        # 友達iの友達jについて探索
        for j in G[i]:
            # jがX(アルル自身)またはアルルの友達である時はスキップ
            if (j == X) or (j in G[X]):
                continue

            # X(アルル)の友達の友達をresultに格納
            result.add(j)
        
    print(len(result))

if __name__ == '__main__':
    main()