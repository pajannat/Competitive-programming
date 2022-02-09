def main():
    from sys import stdin
    input = stdin.readline

    import math

    A, B = map(int, input().split())
    ans = math.gcd(A, B)

    print(ans)

if __name__ == '__main__':
    main()