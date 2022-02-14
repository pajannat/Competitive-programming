def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    accum_A = list(accumulate(A))

    for i in range(Q):
        L, R = map(int, input().split())
        print(accum_A[R]-accum_A[L-1])


if __name__ == '__main__':
    main()