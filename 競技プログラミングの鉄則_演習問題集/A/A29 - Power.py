def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B = map(int, input().split())
    m = 10**9 + 7

    # 処理

    # 答えを出力
    print(pow(A, B, m))


if __name__ == '__main__':
    main()