def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力
    N, X, Y = map(int, input().split())

    # XとYの最小公倍数lcm_XYを求める
    lcm_XY = X*Y // math.gcd(X, Y)

    # 出力
    print(N // lcm_XY)

if __name__ == '__main__':
    main()