def main():
    N, M = map(int, input().split())
    D = list(map(int, input().split()))
    dp = [0]*(2001)

    for d in D:
        dp[d] = 1

    for i in range(N):
        if dp[i] == 1:
            for d in D:
                dp[i+d] = 1

    if dp[N] == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()