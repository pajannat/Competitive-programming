def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split()))

    worse_list = [] # (スコア、何日目か) をペアで持つスタック
    # 0 日目の処理
    worse_list.append([0, 0])
    # i = 1, 2, …, N-1 日目の処理
    for i in range(1, N+1):
        a = A[i]    # i 日目のスコアを a とおく

        # スタックの先頭が本日のスコアより低くなるまで、要素を取り除く
        while a <= worse_list[-1][0]:
            worse_list.pop()

        # 現在の先頭は i 日目の悪い日に関する情報
        # スパンを出力し、本日の情報をスタックに入れる
        ans = i - worse_list[-1][1]
        print(f"score:{a}, span:{ans}, S:{a*ans}")
        worse_list.append([a, i])


if __name__ == '__main__':
    main()