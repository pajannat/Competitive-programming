def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 頂点iのparent
    parent = [-1 for _ in range(N)]
    # 頂点iのchild
    children = [[] for i in range(N)]

    # parent, children に値を格納
    for _ in range(N-1):
        # A:parent, B:child
        A, B = map(int, input().split())

        # Aの子供はBを記録
        children[A].append(B)

        # Bの親はAを記録
        parent[B] = A
    
    for i in range(N):
        children[i].sort()
    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        v = int(input())
        # 頂点vの親　parent[v] が持つchildを出力
        print(*children[parent[v]])


if __name__ == '__main__':
    main()