def main():
    N, M = map(int, input().split())
    D = list(map(int, input().split()))
    dp = [0]*(N+1)

    dp[0] = 1

    for i in range(N+1):
        for d in D:
            if (i-d >= 0) and dp[i-d] == 1:
                dp[i] = 1

    if dp[N] == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()