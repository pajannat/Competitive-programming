def main():
    from sys import stdin
    input = stdin.readline

    import bisect
    from itertools import accumulate

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ruiseki_A = list(accumulate(A))


    # 処理
    for _ in range(Q):
        ans = 0
        X = int(input())

        idx = bisect.bisect_left(A, X)
        if idx == N:
            ans = N*X - ruiseki_A[N-1]
        elif idx == 0:
            ans = ruiseki_A[N-1] - N*X
        else:
            ans = ans + idx*X - ruiseki_A[idx-1]
            ans = ans - (N-idx)*X + (ruiseki_A[N-1] - ruiseki_A[idx-1])

        print(ans)


if __name__ == '__main__':
    main()