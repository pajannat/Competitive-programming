def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    A, B = map(int, input().split())
    ans = (A * B) // math.gcd(A, B)

    if ans > 10**18:
        print("Large")
    else:
        print(ans)

if __name__ == '__main__':
    main()