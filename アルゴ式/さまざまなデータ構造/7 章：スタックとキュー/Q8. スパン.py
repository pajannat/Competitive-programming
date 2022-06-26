def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    worse_list = []

    # 処理
    """
    1. 0日目の処理として worse_list に (0,0) を挿入する
    2. i=1,2,…,N-1 に対し、次の処理をする
    2.1. worse_list の先頭が本日のスコアより低くなるまで、要素を取り除く
    2.2. 先頭の要素は i 日目の悪い日に関するもののため、スパンを出力する
    2.3. (A_i ,i) を worse_list に挿入する
    """
    # 1. 0日目の処理として worse_list に (0,0) を挿入する
    worse_list.append([0, 0])
    # 2. i=1,2,…,N-1 に対し、次の処理をする
    for i in range(1, N):
        A_i = A[i]

        # 2.1. worse_list の先頭が本日のスコアより低くなるまで、要素を取り除く
        while A_i <= worse_list[-1][0]:
            worse_list.pop()

        # 2.2. 先頭の要素は i 日目の悪い日に関するもののため、スパンを出力する
        print(i - worse_list[-1][1])

        # 2.3. (A_i,i) を worse_list に挿入する
        worse_list.append([A_i, i])


if __name__ == '__main__':
    main()