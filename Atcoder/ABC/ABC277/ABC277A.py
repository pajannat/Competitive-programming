def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, X = map(int, input().split())
    P = list(map(int, input().split()))

    # 処理
    for idx, p in enumerate(P):
        if p == X:
            print(idx + 1)


if __name__ == '__main__':
    main()