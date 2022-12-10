def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    for i in range(N, -1, -1):
        print(i)


if __name__ == '__main__':
    main()