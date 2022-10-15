def main():
    from sys import stdin
    input = stdin.readline

    from decimal import Decimal, ROUND_HALF_UP

    # 入力を受け取る
    X, K = map(int, input().split())
    ans = str(X)

    # 処理
    for i in range(1, K+1):
        ans = str(int(Decimal(ans).quantize(Decimal('1E' + str(i)), rounding=ROUND_HALF_UP)))

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()