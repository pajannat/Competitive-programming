def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N = int(input())

    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            ans += i*j

    # εΊε
    print(ans)

if __name__ == '__main__':
    main()