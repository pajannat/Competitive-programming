def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    for k in range(10000):
        if 2**k > N:
            print(k-1)
            break

if __name__ == '__main__':
    main()