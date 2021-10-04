def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    INF = 10**13
    ans = INF
    for i in range(1, N+1):
        # √N で打ち切ってよい
        if i*i > N:
            break

        if N % i != 0:
            continue

        ans = min(ans, i+(N//i))

    print(ans)

if __name__ == '__main__':
    main()