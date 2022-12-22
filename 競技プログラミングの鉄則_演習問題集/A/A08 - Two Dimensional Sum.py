def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    HW = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())

    # 処理
    # タテに累積和
    for i in range(H):
        for j in range(W):
            if i > 0:
                HW[i][j] += HW[i-1][j]
    # ヨコに累積和
    for i in range(H):
        for j in range(W):
            if j > 0:
                HW[i][j] += HW[i][j-1]

    # 答えを出力
    # 左上 HW[A][B], 右下 HW[C][D] の領域の総和を計算する
    for i in range(Q):
        A, B, C, D = map(int, input().split())
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        ans = 0
        ans += HW[C][D]
        if B > 0:
            ans -= HW[C][B-1]
        if A > 0:
            ans -= HW[A-1][D]
        if B > 0 and A > 0:
            ans += HW[A-1][B-1]
        print(ans)


if __name__ == '__main__':
    main()