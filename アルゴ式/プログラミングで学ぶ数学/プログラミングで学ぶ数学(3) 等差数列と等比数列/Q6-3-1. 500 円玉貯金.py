def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, X = map(int, input().split())
    ans = X

    # εΊε
    print(ans)
    for i in range(N):
        ans += 500
        print(ans)

if __name__ == '__main__':
    main()