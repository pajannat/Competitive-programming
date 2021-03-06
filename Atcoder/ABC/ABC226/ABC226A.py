def main():
    from sys import stdin
    input = stdin.readline

    from decimal import Decimal, ROUND_HALF_UP

    # ε₯ε
    X = input().rstrip()

    # εΊε
    print(Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    main()