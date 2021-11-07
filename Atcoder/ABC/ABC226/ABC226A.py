def main():
    from sys import stdin
    input = stdin.readline

    from decimal import Decimal, ROUND_HALF_UP

    # 入力
    X = input().rstrip()

    # 出力
    print(Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    main()