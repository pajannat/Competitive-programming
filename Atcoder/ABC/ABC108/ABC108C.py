def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())

    # 処理
    
    # 答えを出力
    if K % 2 == 0:
        print((N // K) ** 3 + (((N - K//2) // K) + 1) ** 3)
    else:
        print((N // K) ** 3)


if __name__ == '__main__':
    main()