def main():
    from sys import stdin
    input = stdin.readline

    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[0]*(S+1) for i in range(N+1)]

    dp[0][0] = 1

    for i in range(1, N+1):
        num = i - 1
        for j in range(S+1):
            if j >= A[num]:
                if dp[i-1][j-A[num]] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-A[num]]
            else:
                dp[i][j] = dp[i-1][j]

    if dp[-1][-1] != 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()