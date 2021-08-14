def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort()
    B_list.sort()
    min1 = 10**10
    min_min = 10**10

    for a in A_list:
        # B_listの値のうち、aに近い値を二分探索で探す
        index = bisect.bisect_right(B_list, a)
        # a前後の値と比較して、小さいほうをmin1に保持
        min1 = min(abs(a-B_list[min(index, M-1)]), min1)
        min1 = min(abs(a-B_list[min(index-1, M-1)]), min1)

        min_min = min(min_min, min1)

    print(min_min)

if __name__ == '__main__':
    main()