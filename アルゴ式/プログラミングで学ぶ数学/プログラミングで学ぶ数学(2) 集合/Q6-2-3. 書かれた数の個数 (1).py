def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, X = map(int, input().split())

    # εΊε
    print(N // X)

if __name__ == '__main__':
    main()