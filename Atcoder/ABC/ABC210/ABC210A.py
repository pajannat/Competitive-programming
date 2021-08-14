def main():
    from sys import stdin
    input = stdin.readline

    N, A, X, Y = map(int, input().split())

    ans = 0
    if N > A:
        ans = A*X + (N - A)*Y
    else:
        ans = N*X

    print(ans)

if __name__ == '__main__':
    main()