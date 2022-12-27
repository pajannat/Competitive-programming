def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    # Aの要素をソートして重複削除したlist T
    T = list(set(A))  # Aの重複を削除
    T.sort()  # Tを昇順にソート
    B = [None] * N


    # 処理

    for i in range(N):
        # A[i] がAの中で何番目の大きさか, bisect.bisect_left(T, a)で調べる
        # B[i]にbisect.bisect_left(T, a) を格納
        B[i] = bisect.bisect_left(T, A[i]) + 1

    # 答えを出力
    print(*B)


if __name__ == '__main__':
    main()