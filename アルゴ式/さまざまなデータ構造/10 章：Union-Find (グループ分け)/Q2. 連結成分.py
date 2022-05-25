def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフなので、頂点 B から頂点 A へも張る
        G[B].append(A)

    from collections import deque
    d = deque()

    # 各頂点が探索済みかを表す配列
    used = [False] * N

    # 連結成分の数をカウント
    ans = 0
    for i in range(N):
        # 探索済みの場合はスキップ
        if used[i]:
            continue

        # 頂点iに連なる頂点をすべて探索済みにする
        used[i] = True
        d.append(i)
        while d:
            v = d.popleft()

            for j in G[v]:
                # 探索済みの頂点はスキップ
                if used[j]:
                    continue
                # 次の探索先に加える
                d.append(j)
                used[j] = True
        ans += 1

    # 出力
    print(ans)

if __name__ == '__main__':
    main()