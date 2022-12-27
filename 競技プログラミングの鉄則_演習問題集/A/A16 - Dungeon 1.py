def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = [0, 0] + list(map(int, input().split()))
    B = [0, 0, 0] + list(map(int, input().split()))
    dp = [10**7 + 5] * (N+1)

    # 処理
    dp[0] = 0
    dp[1] = 0
    dp[2] = dp[1] + A[2]
    for i in range(3, N+1):
        dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])
    
    # 答えを出力
    print(dp[-1])


if __name__ == '__main__':
    main()