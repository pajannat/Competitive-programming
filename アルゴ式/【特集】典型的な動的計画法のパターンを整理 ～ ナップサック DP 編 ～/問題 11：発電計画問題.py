def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    T = int(input())
    g = [list(map(int, input().split())) for _ in range(T)]

    # 配列全体を 0 に初期化しておく
    dp = [0]*(T+2)
    for t in range(T+2):
        for i in range(t-1):
            for j in range(i+1, t):
                dp[t] = max(dp[t], dp[i]+g[i][j-1])
  
    print(dp[-1])

if __name__ == '__main__':
    main()