def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W, N = map(int, input().split())
    HW = [[0]*(W+1) for _ in range(H+1)]
    for i in range(N):
        A, B, C, D = map(int, input().split())
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        HW[A][B] += 1
        HW[A][D+1] -= 1
        HW[C+1][B] -= 1
        HW[C+1][D+1] += 1

    # 処理
    # ヨコに累積和
    for i in range(H+1):
        for j in range(W+1):
            if j > 0:
                HW[i][j] += HW[i][j-1]
    # タテに累積和
    for i in range(H+1):
        for j in range(W+1):
            if i > 0:
                HW[i][j] += HW[i-1][j]

    # 答えを出力
    for i in range(H):
        print(*HW[i][:-1])


if __name__ == '__main__':
    main()