def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = list(map(int, input().split()))

    A.sort()

    # εΊε
    for x in X:
        print(A[x])


if __name__ == '__main__':
    main()