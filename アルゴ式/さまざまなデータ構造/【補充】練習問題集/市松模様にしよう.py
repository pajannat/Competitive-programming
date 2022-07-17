def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    masu = [list(input().rstrip()) for _ in range(H)]

    cnt = 10**7
    # マス (x, y) について,
    # x+y % 2 == 0 となるマスが "#", x+y % 2 == 1 となるマスが "." のとき
    tmp_cnt = 0
    for x in range(H):
        for y in range(W):
            if (x+y) % 2 == 0:
                # masu[x][y] が "#" でなければマスを反転
                if masu[x][y] != "#":
                    tmp_cnt += 1
                    
            elif (x+y) % 2 == 1:
                # masu[x][y] が "." でなければマスを反転
                if masu[x][y] != ".":
                    tmp_cnt += 1
    
    cnt = min(cnt, tmp_cnt)

    # マス (x, y) について, 
    # x+y % 2 == 0 となるマスが ".", x+y % 2 == 1 となるマスが "#" のとき
    tmp_cnt = 0
    for x in range(H):
        for y in range(W):
            if (x+y) % 2 == 0:
                # masu[x][y] が "." でなければマスを反転
                if masu[x][y] != ".":
                    tmp_cnt += 1
                    
            elif (x+y) % 2 == 1:
                # masu[x][y] が "#" でなければマスを反転
                if masu[x][y] != "#":
                    tmp_cnt += 1
    
    cnt = min(cnt, tmp_cnt)

    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()