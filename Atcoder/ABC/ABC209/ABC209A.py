def main():
    from sys import stdin
    input = stdin.readline

    from itertools import permutations
    import math

    A,B = map(int,input().split())

    if B >= A:
        ans = B - A + 1
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    main()