def main():
    from sys import stdin
    input = stdin.readline

    X = int(input())
    A = list(map(int, input().split()))
    coins = [50, 10, 5, 1]

    cnt = 0

    for i in range(len(coins)):
        add = min(X // coins[i], A[i])
        cnt += add

        X -= coins[i]*add

    print(cnt)

if __name__ == '__main__':
    main()