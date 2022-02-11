def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += A[i]*(1/3) + B[i]*(2/3)

    print(ans)

if __name__ == '__main__':
    main()