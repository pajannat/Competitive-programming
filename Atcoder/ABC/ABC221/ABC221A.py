def main():
    from sys import stdin
    input = stdin.readline

    A, B = map(int, input().split())
    ans = 1
    ans = ans*(32**(A-B))

    print(ans)

if __name__ == '__main__':
    main()