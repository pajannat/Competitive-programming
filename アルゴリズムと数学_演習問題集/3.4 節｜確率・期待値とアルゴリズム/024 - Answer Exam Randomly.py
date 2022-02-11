def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    ans = 0
    for i in range(N):
        P, Q = map(int, input().split())
        ans += Q / P

    print(ans)

if __name__ == '__main__':
    main()