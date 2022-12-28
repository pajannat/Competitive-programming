def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0]*(10**4 + 1) for _ in range(N+1)]

    # 処理
    dp[0][0] = 1
    for i in range(N):
        for j in range(len(dp[i])):
            if dp[i][j] == 1:
                # 下に配る
                dp[i+1][j] = 1
                # 右下に配る
                if j+A[i] < len(dp[i]):
                    dp[i+1][j+A[i]] = 1

    
    # 答えを出力
    if dp[-1][S] == 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()