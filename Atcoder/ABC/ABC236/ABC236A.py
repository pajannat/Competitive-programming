def main():
    from sys import stdin
    input = stdin.readline

    S = list(input().rstrip())
    A, B = map(int, input().split())

    ans = ''.join(S[:(A-1)]) + ''.join(S[B-1]) + ''.join(S[A:(B-1)]) + ''.join(S[A-1]) + ''.join(S[B:])

    print(ans)

if __name__ == '__main__':
    main()