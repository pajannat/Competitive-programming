def main():
    from sys import stdin
    input = stdin.readline
    import math
    from decimal import Decimal

    N = int(input())

    a = Decimal(N // 2)
    c = Decimal(N % 2)
    b = 1

    abc_sum = a+b+c

    for i in range(62):
        tmp_a = N // (2**i)
        tmp_c = N % (2**i)
        tmp_b = i
        tmp_abc_sum = tmp_a + tmp_b + tmp_c
        if tmp_abc_sum < abc_sum:
            a = tmp_a
            b = tmp_b
            c = tmp_c
            abc_sum = a + b + c

    print(abc_sum)   

if __name__ == '__main__':
    main()