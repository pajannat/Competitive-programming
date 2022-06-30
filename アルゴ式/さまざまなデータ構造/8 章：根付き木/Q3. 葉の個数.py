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

    # 葉の数をカウント
    ans = 0
    for i in range(1, N):
        # childを持たない頂点(葉)であればカウント
        if len(children[i]) == 0:
            ans += 1
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()