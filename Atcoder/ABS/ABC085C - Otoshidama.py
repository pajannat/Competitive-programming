def main():
    from sys import stdin
    input = stdin.readline
    N, Y = map(int,input().split())

    sum = 0
    flg = False
    for idx1 in range(N+1):
        if flg:
            break
        for idx2 in range(N+1-idx1):
            sum = 10000*idx1 + 5000*idx2 + 1000*(N-idx1-idx2)
            if sum == Y:
                flg = True
                A = idx1
                B = idx2
                C = N-idx1-idx2
                break

    if flg:
        print(A,B,C)
    else:
        print(-1,-1,-1)

if __name__ == '__main__':
    main()