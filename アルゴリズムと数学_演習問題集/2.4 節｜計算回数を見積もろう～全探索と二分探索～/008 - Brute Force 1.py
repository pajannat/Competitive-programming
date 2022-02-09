def main():
    from sys import stdin
    input = stdin.readline

    cnt = 0
    N, S = map(int, input().split())
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i+j <= S:
                cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()