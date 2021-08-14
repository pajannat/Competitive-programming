def main():
    from sys import stdin
    input = stdin.readline

    import collections

    N = int(input())
    A_list = list(map(int,input().split()))

    c = collections.Counter(A_list).values()
    sum = 0
    for num in c:
        sum += num * (N-num)
    ans = int(sum / 2)
    print(ans)

if __name__ == '__main__':
    main()