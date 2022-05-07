def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # 処理
    masu = [['.']*(S-R+1) for _ in range(Q-P+1)]

    # max(P-A,R-B)≤k≤min(Q-A,S-B) をみたす全ての整数 k について、
    # (A+k,B+k) を黒く塗る。
    min1 = max(P-A, R-B)
    max1 = min(Q-A, S-B)
    for k in range(min1, max1+1):
        if (0 <= A+k-P <= Q-P+1) and (0 <= B+k-R <= S-R+1):
            masu[A+k-P][B+k-R] = '#'

    # max(P-A,B-S)≤k≤min(Q-A,B-R) をみたす全ての整数 k について、
    # (A+k,B−k) を黒く塗る。
    min2 = max(P-A, B-S)
    max2 = min(Q-A, B-R)
    for k in range(min2, max2+1):
        if (0 <= A+k-P <= Q-P+1) and (0 <= B-k-R <= S-R+1):
            masu[A+k-P][B-k-R] = '#'

    # 答えを出力
    for m in masu:
        print("".join(m))


if __name__ == '__main__':
    main()