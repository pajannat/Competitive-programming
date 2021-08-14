def main():
    from sys import stdin
    input = stdin.readline

    A, B = map(int, input().split())

    print(A ^ B)

if __name__ == '__main__':
    main()