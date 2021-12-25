def main():
    from sys import stdin
    input = stdin.readline

    import itertools

    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    LL = [l[1:] for l in L]

    cnt = 0

    p = itertools.product(*LL)
    for a in p:
        tmp = 1
        for n in a:
            tmp *= n
        if tmp == X:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()