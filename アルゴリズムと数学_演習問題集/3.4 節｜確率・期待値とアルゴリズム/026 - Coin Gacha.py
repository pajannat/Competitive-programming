def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    ans = 0
    for i in range(N):
        ans += N/(N-i)

    print(ans)

if __name__ == '__main__':
    main()