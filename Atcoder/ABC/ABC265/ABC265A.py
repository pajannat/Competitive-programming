def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    X, Y, N = map(int, input().split())
    ans = 10**5

    # 処理
    # りんご3個あたりの値段が 3X円 <= Y円 の場合
    if 3*X <= Y:
        # 1個あたりの値段がXで購入したほうが安いので、N個すべてX円で購入
        ans = X*N
    else:
        ans = (N - 3*(N//3))*X + (N//3)*Y

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()