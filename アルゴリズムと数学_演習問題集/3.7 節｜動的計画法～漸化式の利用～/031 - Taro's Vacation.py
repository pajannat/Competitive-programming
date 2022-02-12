def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [0]*(N+1)

    dp[1] = A[1]
    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+A[i])

    print(dp[N])

if __name__ == '__main__':
    main()