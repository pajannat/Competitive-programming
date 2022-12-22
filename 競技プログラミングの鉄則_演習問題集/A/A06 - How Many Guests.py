def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和
    accum_A = [0] + list(accumulate(A))

    # 処理
    for _ in range(Q):
        L, R = map(int, input().split())
        print(accum_A[R] - accum_A[L-1])


if __name__ == '__main__':
    main()