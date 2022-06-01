def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    dxdy = [[0,0], [0,1], [0,-1], [1,0], [-1,0]]

    grid = [[0]*W for _ in range(H)]
    for h in range(H):
        S = input().rstrip()
        for w, s in enumerate(S):
            if s == "#":
                grid[h][w] = 1
            else:
                grid[h][w] = 0
    
    # 前処理
    cnt_all = 0
    for h in range(H):
        for w in range(W):
            cnt_all += grid[h][w]
    
    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            flg, p, q = query[0], query[1], query[2]
        else:
            flg = query[0]

        # push query
        if flg == 0:
            cnt = 0
            change_cnt = 0
            for dx, dy in dxdy:
                if (0<=p+dy<=H-1) and (0<=q+dx<=W-1):
                    cnt += 1
                    change_cnt += grid[p+dy][q+dx]
                    grid[p+dy][q+dx] = 1 - grid[p+dy][q+dx]
            cnt_all += cnt - 2*change_cnt

        # get query
        if flg == 1:
            print(cnt_all)


if __name__ == '__main__':
    main()