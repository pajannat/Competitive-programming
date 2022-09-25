def main():
    from sys import stdin
    input = stdin.readline

    from sys import setrecursionlimit
    setrecursionlimit(10000000)  # RecursionError対策

    # 入力を受け取る
    N, X, Y = map(int, input().split())

    adj = [[] for i in range(N+1)]
    for i in range(1, N):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)

    # 発見時刻
    d = [0] * (N+1)
    # 完了時刻
    f = [0] * (N+1)
    # 探索開始点Xから探索終了点Yまでの経路
    path = []

    # ノード v , 時刻 t から深さ優先探索する関数
    def dfs(v, t):
        t += 1 # 発見したらインクリメント
        d[v] = t
        # 経路を記録
        path.append(v)
        # 探索終了点Yに到達したら終了
        if v == Y:
            # 経路を出力
            print(*path)
            # 探索を終了
            exit
        # 頂点vに隣接するv1,v2,...を探索
        for next in adj[v]:
            # 未発見なら
            if d[next] == 0:
                t = dfs(next, t)
        # 完了してもインクリメント
        t += 1
        f[v] = t
        # 葉に到達したらpathからpop
        path.pop()
        return t

    # 処理
    dfs(X, 0)


if __name__ == '__main__':
    main()