def main():
    from sys import stdin
    input = stdin.readline

    L = int(input())
    import math
    print(math.comb(L-1,11))

if __name__ == '__main__':
    main()