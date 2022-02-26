def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    print(len(set(A)))

if __name__ == '__main__':
    main()