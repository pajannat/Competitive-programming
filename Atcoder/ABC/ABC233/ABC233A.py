def main():
    from sys import stdin
    input = stdin.readline

    import math

    X, Y = map(int, input().split())
    tmp = Y - X
    if tmp <= 0:
        print(0)
    else:
        ans = math.ceil(tmp/10)
        print(ans)

if __name__ == '__main__':
    main()