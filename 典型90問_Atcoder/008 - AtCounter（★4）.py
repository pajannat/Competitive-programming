def main():
    from sys import stdin
    input = stdin.readline

    MOD = 10**9 + 7
    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # dp[atcoderの何文字目か?][Sの何文字目か?]
    dp = [[0]*(N+1) for j in range(8)] # DPテーブルの作成

    # 処理
    for i in range(N+1):
        dp[0][i] = 1

    for i in range(1, len(S)+1):
        for j in range(1, 8):
            # 左からもらう
            dp[j][i] = (dp[j][i] + dp[j][i-1]) % MOD

            # 左上からもらう条件分岐
            if j == 1 and S[i-1] == "a":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 2 and S[i-1] == "t":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 3 and S[i-1] == "c":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 4 and S[i-1] == "o":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 5 and S[i-1] == "d":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 6 and S[i-1] == "e":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD
            elif j == 7 and S[i-1] == "r":
                dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % MOD

    # 答えを出力
    print(dp[-1][-1])

if __name__ == '__main__':
    main()