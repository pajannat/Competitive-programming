def main():
    A0, A1, A2, A3 = map(int, input().split())
    dp = [[0]*4 for _ in range(4)]

    dp[0][0] = A0
    dp[0][1] = A1
    dp[0][2] = A2
    dp[0][3] = A3

    for i in range(1, 4):
        for j in range(4):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == 3:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

    print(dp[-1][-1])

if __name__ == '__main__':
    main()