def main():
    from sys import stdin
    input = stdin.readline

    A, B, C = map(int, input().split())
    ans = -1

    for i in range(1000):
        ans = int(i*C)

        if A <= ans <= B:
            break
    
    if A <= ans <= B:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()