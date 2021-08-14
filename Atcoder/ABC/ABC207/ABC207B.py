def main():
    from sys import stdin
    input = stdin.readline

    import math

    A,B,C,D = map(int,input().split())

    if D*C-B <= 0:
        print(-1)
    else:
        print(math.ceil(A/(D*C-B)))


if __name__ == '__main__':
    main()