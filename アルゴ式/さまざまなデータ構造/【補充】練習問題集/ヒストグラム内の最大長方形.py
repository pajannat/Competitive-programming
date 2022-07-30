def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # 左方向に伸ばせる限界の位置
    lower_left = [0 for _ in range(N)]
    # 右方向に伸ばせる限界の位置
    lower_right = [0 for _ in range(N)]
    # ヒストグラム内の最大長方形の面積
    S_max = 0


    # i番目の高さが入る最大の長方形を作る
    # i番目の高さを左端とする
    # i番目の高さより低くなったら長方形が入らないので打ち切り
    # 右方向へと順に高さを調べていく

    worse_list_left = [] # (高さ、何番目か) をペアで持つスタック
    # N 番目の処理(番兵)
    worse_list_left.append([0, N])
    # i = N-1, N-2, …, 0 番目の処理
    for i in range(N-1, 0, -1):
        A_i = A[i]    # i 日目のスコアを a とおく

        # スタックの先頭がA_iより低くなるまで、要素を取り除く
        # (低い高さのものを探索していくので、
        # (より高いものが格納されていても意味がない
        while A_i <= worse_list_left[-1][0]:
            worse_list_left.pop()

        # ↑の処理の結果、現在の先頭は A_iより低いときの情報
        # i番目から順にみて、初めてA_iより低くなったとき

        # lower_left[i] を記録して、
        # i+1番目の処理に向け, i番目の情報(A_i, i) をスタックに入れる
        lower_left[i] = worse_list_left[-1][1]

        # i+1番目の処理に向け, i番目の情報(A_i, i) をスタックに入れる
        worse_list_left.append([A_i, i])


    # i番目の高さが入る最大の長方形を作る
    # i番目の高さを右端とする
    # i番目の高さより低くなったら長方形が入らないので打ち切り
    # 左方向へと順に高さを調べていく

    worse_list_right = [] # (高さ、何番目か) をペアで持つスタック
    # -1 番目の処理(番兵)
    worse_list_right.append([0, -1])
    # i = 0, 1, …, N-1 番目の処理
    for i in range(0, N):
        A_i = A[i]    # i 番目の高さを A_i とおく

        # スタックの先頭がA_iより低くなるまで、要素を取り除く
        # (低い高さのものを探索していくので、
        # (より高いものが格納されていても意味がない
        while A_i <= worse_list_right[-1][0]:
            worse_list_right.pop()

        # ↑の処理の結果、現在の先頭は A_iより低いときの情報
        # (i番目から順にみて、初めてA_iより低くなったとき

        # lower_right[i] を記録して、
        # i+1番目の処理に向け, i番目の情報 (A_i, i) をスタックに入れる
        lower_right[i] = worse_list_right[-1][1]
        worse_list_right.append([A_i, i])
    

    for i in range(N):
        a = A[i]
        l, r = lower_left[i], lower_right[i]

        # i 番目の長方形を完全に包含する最大の長方形は「高さ a 、幅 l - r - 1」
        # その面積が ans より大きいなら、ans を更新する
        S = a * (l - r - 1)
        S_max = max(S_max, S)

    # 答えを出力
    print(S_max)


if __name__ == '__main__':
    main()