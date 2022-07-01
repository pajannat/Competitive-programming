def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 頂点iのparent
    P = [-1] + list(map(int, input().split()))
    # ある箱の番号 v
    v = int(input())
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
    cnt = 0

    # 行きがけ順で箱を記録
    def rec(v, children):
        nonlocal cnt
        # 箱vを開けた時に現れる箱(ただし番号が小さい順)を開ける
        for v2 in children[v]:
            # 箱を開けたらcnt+=1
            cnt += 1
            rec(v2, children)
        # 帰りがけ順で番号 v を記録する
        # 関数終了時、関数から抜ける直前に記録
        rec_list.append(v)
    
    # vの箱から開ける
    rec(v, children)
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()