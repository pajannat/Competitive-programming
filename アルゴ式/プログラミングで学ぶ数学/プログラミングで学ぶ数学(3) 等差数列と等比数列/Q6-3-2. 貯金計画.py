def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    A, B, X, Y = map(int, input().split())
    C = (Y-X)/(B-A)

    # εΊε
    print(int(X-A*C))

if __name__ == '__main__':
    main()