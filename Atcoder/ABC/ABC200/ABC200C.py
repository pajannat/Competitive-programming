def main():
    from sys import stdin
    input = stdin.readline
    
    N = int(input())
    list_A = list(map(int,input().split()))

    B = []
    cnt = 0
    for i in range(100):
        for A in list_A:
            if A % 100 == i:
                B.append(A)
    for comb in itertools.combinations(B, 2):
        if (comb[0]-comb[1])%200 == 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()