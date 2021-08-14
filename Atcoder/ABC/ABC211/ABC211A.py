def main():
    from sys import stdin
    input = stdin.readline

    A, B = map(int, input().split())
    C = (A-B)/3 + B

    print(C)

if __name__ == '__main__':
    main()