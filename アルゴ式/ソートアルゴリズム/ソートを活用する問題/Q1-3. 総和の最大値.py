def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    # εΊε
    print(sum(A[:K]))

if __name__ == '__main__':
    main()