def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, X = map(int, input().split())

    # 出力
    print(N // X)

if __name__ == '__main__':
    main()