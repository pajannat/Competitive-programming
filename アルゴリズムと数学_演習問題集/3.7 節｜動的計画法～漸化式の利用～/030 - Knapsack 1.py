def main():
    from sys import stdin
    input = stdin.readline

    N, W = map(int, input().split())

    Goods = [[0, 0]]
    for i in range(N):
        w, v = map(int, input().split())
        Goods.append([w, v])

    dp = [[0]*(W+1) for _ in range(N+1)]

    for n in range(1, N+1):
        for w in range(W+1):
            if w-Goods[n][0] < 0:
                dp[n][w] = dp[n-1][w]
            else:
                dp[n][w] = max(dp[n-1][w], dp[n-1][w-Goods[n][0]]+Goods[n][1])

    print(max(dp[-1]))

if __name__ == '__main__':
    main()