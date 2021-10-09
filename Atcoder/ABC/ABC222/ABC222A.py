def main():
    from sys import stdin
    input = stdin.readline

    N = input().rstrip()

    if len(N) == 1:
        ans = "000" + N
    elif len(N) == 2:
        ans = "00" + N
    elif len(N) == 3:
        ans = "0" + N
    else:
        ans = N
    
    print(ans)

if __name__ == '__main__':
    main()