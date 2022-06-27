def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 頂点iのparent
    P = [-1] + list(map(int, input().split()))
    # 頂点iのchild
    child_list = [[] for i in range(N)]

    # child_list に値を格納
    for i in range(N):
        # i == 0 はスキップ
        if i == 0:
            continue

        A = i
        B = P[i]

        # 無向グラフの場合は次も実施
        child_list[B].append(A)
    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        v = int(input())
        # 頂点vの親　P[v] が持つchildを出力
        print(*child_list[P[v]])


if __name__ == '__main__':
    main()