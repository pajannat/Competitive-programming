def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 隣接行列 adj
    adj = [[] for i in range(N)]

    # 隣接行列 adj に値を格納
    for _ in range(N-1):
        A, B = map(int, input().split())

        adj[A].append(B)
        adj[B].append(A)

    # 頂点iのparent
    parent = [-1 for _ in range(N)]
    # 頂点iのchild
    children = [[] for _ in range(N)]

    # adj[v] に格納されている各頂点が
    # parentかchildかを判別する関数rec
    def rec(v, parent_v, children, parent):
        # vn がparentかchildかを判別
        for vn in adj[v]:
            # vnが頂点vのparentでなければchild
            if vn != parent_v:
                children[v].append(vn)
                parent[vn] = v
                # vnについてrec(vn, v)
                rec(vn, v, children, parent)

    # 根0から探索開始
    rec(0, -1, children, parent)

    # children を昇順にsort
    for i in range(N):
        children[i].sort()

    # クエリの数
    Q = int(input())
    # クエリ処理
    for _ in range(Q):
        # クエリを受け取る
        v = int(input())
        # 頂点vのparentを取得
        parent_v = parent[v]
        # 答えを出力
        print(*children[parent_v])


if __name__ == '__main__':
    main()