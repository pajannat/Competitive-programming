def main():
    from sys import stdin
    input = stdin.readline

    S, T = map(int, input().split())
    
    cnt = 0
    for a in range(101):
        for b in range(101):
            for c in range(101):
                if (a+b+c <= S) and (a*b*c <= T):
                    cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()