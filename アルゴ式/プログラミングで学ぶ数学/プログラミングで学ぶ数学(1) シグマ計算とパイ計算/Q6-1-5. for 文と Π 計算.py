def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N = int(input())
    A = list(map(int, input().split()))

    ans = 1
    for i in range(N):
        ans = (ans * A[i]) % 10

    # εΊε
    print(ans)

if __name__ == '__main__':
    main()