def main():
    from sys import stdin
    input = stdin.readline

    H,W = map(int,input().split())
    S = [list(input().rstrip()) for _ in range(H) ] 

    kado = 0
    for h in range(H-1):
        for w in range(W-1):
            cnt = 0
            if S[h][w] == '#':
                cnt += 1
            if S[h][w+1] == '#':
                cnt += 1
            if S[h+1][w] == '#':
                cnt += 1
            if S[h+1][w+1] == '#':
                cnt += 1
            if cnt ==1 or cnt ==3:
                kado += 1

    print(kado)

if __name__ == '__main__':
    main()