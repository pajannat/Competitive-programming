def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    A, B, X, Y = map(int, input().split())
    C = (Y-X)/(B-A)

    # 出力
    print(int(X-A*C))

if __name__ == '__main__':
    main()