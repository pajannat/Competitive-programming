def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A_list = list(map(int, input().split()))

    # タプルのソートは1要素目の大小でソート。
    order_list = [(A_list[i], i) for i in range(0, len(A_list))]
    order_list.sort(reverse=True)

    print(order_list[1][1]+1)

if __name__ == '__main__':
    main()