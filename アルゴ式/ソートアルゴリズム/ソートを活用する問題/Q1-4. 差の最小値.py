def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    diff = 10**10
    for i in range(N-K+1):
        diff = min(diff, A[i+K-1]-A[i])

    # εΊε
    print(diff)

if __name__ == '__main__':
    main()