def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 頂点iのparent
    P = [-1] + list(map(int, input().split()))
    # 頂点iのchild
    children = [[] for i in range(N)]

    # children に値を格納
    for i in range(N):
        # i == 0 はスキップ
        if i == 0:
            continue

        A = i
        B = P[i]

        # parent Bの childに Aを追加
        children[B].append(A)

    for i in range(N):
        children[i].sort()

    rec_list = []
    # 行きがけ順で箱を開ける
    def rec(v, children):
        # 番号 v を記録する
        rec_list.append(v)
        # 箱vを開けた時に現れる箱(ただし番号が小さい順)を開ける
        for v2 in children[v]:
            rec(v2, children)
    
    # 0の箱から開ける
    rec(0, children)
    
    # 答えを出力
    print(*rec_list)


if __name__ == '__main__':
    main()