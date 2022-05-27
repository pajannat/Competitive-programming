def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    dxdy = [[0,0], [0,1], [0,-1], [1,0], [-1,0]]

    grid = [[0]*W for _ in range(H)]
    for h in range(H):
        S = input().rstrip()
        for w in range(W):
            if S[w] == "#":
                grid[h][w] = 1
            else:
                grid[h][w] = 0
    
    # 処理
    Q = int(input())
    for _ in range(Q):
        flg, p, q = map(int, input().split())
        # push query
        if flg == 0:
            for dx, dy in dxdy:
                if (0<=p+dy<=H-1) and (0<=q+dx<=W-1):
                    grid[p+dy][q+dx] = 1 - grid[p+dy][q+dx]

        # get query
        if flg == 1:
            cnt = 0
            for dx, dy in dxdy:
                if (0<=p+dy<=H-1) and (0<=q+dx<=W-1):
                    cnt += grid[p+dy][q+dx]
            
            print(cnt)


if __name__ == '__main__':
    main()