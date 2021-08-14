def main():
    from sys import stdin
    input = stdin.readline

    from collections import Counter

    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    S = Counter(C)

    ans = 1
    cnt = 0
    MOD = 10**9 + 7
    for c, kosu in S.items():
        n = c - cnt
        r = kosu
        if (n | r) <= 0:
            ans = 0
            break
        for i in range(kosu):
            ans *= (c - cnt - i)
            ans = ans % MOD
        cnt += kosu

    print(int(ans))

if __name__ == '__main__':
    main()