def main():
    from sys import stdin
    input = stdin.readline
 
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0]*N for _ in range(N)]
    dp[0] = A

    for i in range(1, N):
        for j in range(N):
            if j == 0:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % 100
            elif j == N-1:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 100
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % 100

    print(dp[-1][-1])
 
if __name__ == '__main__':
    main()