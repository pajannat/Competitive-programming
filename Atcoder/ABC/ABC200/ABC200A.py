def main():
    from sys import stdin
    input = stdin.readline
        
    N = int(input())
    import math
    print(math.ceil(N/100))


if __name__ == '__main__':
    main()