def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, M = map(int, input().split())

    G = [[] for i in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        G[B].append(A)

    # 処理
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                # 同じ頂点を2つ以上選ぶ場合はスキップ
                if (a==b) or (b==c) or (c==a) or (a==b and b==c):
                    continue

                if (b in G[a]) and (c in G[b]) and (a in G[c]):
                    cnt += 1

    # 答えを出力
    print(cnt//6)


if __name__ == '__main__':
    main()