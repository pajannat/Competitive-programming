def main():
    from sys import stdin
    input = stdin.readline

    L, R = map(int, input().split())
    S = input().rstrip()

    tmp = S[L-1:R]

    ans = S[:L-1] + tmp[::-1] + S[R:]

    print(ans)

if __name__ == '__main__':
    main()