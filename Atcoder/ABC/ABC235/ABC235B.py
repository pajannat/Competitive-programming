def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    H = list(map(int, input().split()))

    ans = H[0]

    for h in H[1:]:
        if ans >= h:
            break
        ans = h

    print(ans)

if __name__ == '__main__':
    main()