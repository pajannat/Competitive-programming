def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # 答えを出力
    for i in range(Q):
        x = int(input())
        idx = bisect.bisect_left(A, x)
        print(N-idx)

if __name__ == '__main__':
    main()