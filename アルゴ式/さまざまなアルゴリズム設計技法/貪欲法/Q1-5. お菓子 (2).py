def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())

    cnt = 0
    while N != 0:
        if (N % 3) == 0:
            N = N // 3
            cnt += 1
        else:
            N -= 1
            cnt += 1

    # 答えを出力
    print(cnt)

if __name__ == '__main__':
    main()