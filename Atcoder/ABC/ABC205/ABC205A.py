def main():
    from sys import stdin
    input = stdin.readline

    A,B = map(int,input().split())

    print(A/100*B)


if __name__ == '__main__':
    main()