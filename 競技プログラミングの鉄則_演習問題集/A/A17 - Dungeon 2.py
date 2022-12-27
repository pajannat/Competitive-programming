def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = [0, 0] + list(map(int, input().split()))
    B = [0, 0, 0] + list(map(int, input().split()))
    dp = [10**7 + 5] * (N+1)
    route = []

    # 処理
    dp[1] = 0
    dp[2] = dp[1] + A[2]
    for i in range(3, N+1):
        dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])
    
    route.append(N)
    place = N
    while True:
        if place == 1:
            break

        if dp[place-1]+A[place] < dp[place-2]+B[place]:
            place -= 1
            route.append(place)
        else:
            place -= 2
            route.append(place)
    
    # 答えを出力
    route.sort()
    print(len(route))
    print(*route)


if __name__ == '__main__':
    main()