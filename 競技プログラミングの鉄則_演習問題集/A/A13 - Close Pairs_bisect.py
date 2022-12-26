def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    # 処理
    for i in range(N-1, -1, -1):
        # 各A[i]に対して、A[i]-A[l_idx] <= K となるl_idxを二分探索
        l_idx = bisect.bisect_left(A, (A[i]-K), lo=0, hi=i)
        ans += (i - l_idx)


    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()