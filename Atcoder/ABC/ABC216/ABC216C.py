def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    S = []
    while N != 0:
        if N % 2 == 0:
            N = N // 2
            S.append("B")
        else:
            N = N - 1
            S.append("A")
    S.reverse()
    ans = ''.join(S)
    
    print(ans)

if __name__ == '__main__':
    main()