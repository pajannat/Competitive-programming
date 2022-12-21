def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    ans = 0

    # 処理
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 1 <= K-i-j <= N:
                ans += 1

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()