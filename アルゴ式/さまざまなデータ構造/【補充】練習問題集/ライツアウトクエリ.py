def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    H, W = map(int, input().split())
    # マス目を格納
    masu = []
    for r in range(H):
        s = list(input().rstrip())
        masu.append(s)
    
    # row h の黒マスの数
    sum_row = [0] * H
    for h in range(H):
        cnt = 0
        for color in masu[h]:
            if color == "#":
                cnt += 1
        sum_row[h] = cnt

    # column w の黒マスの数
    sum_column = [0] * W
    for w in range(W):
        cnt = 0
        for h in range(H):
            color = masu[h][w]
            if color == "#":
                cnt += 1
        sum_column[w] = cnt

    # 差分を表す配列
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, 1, 0, -1]

    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])
        p, q = int(query[1]), int(query[2])\

        # Push query
        if flg == 0:
            for i in range(5):
                x, y = p + dx[i], q + dy[i]

                if (0 <= x <= H-1) and (0 <= y <= W-1):
                    if masu[x][y] == "#":
                        masu[x][y] = "."
                        sum_row[x] -= 1
                        sum_column[y] -= 1
                    else:
                        masu[x][y] = "#"
                        sum_row[x] += 1
                        sum_column[y] += 1

        # GetNum query
        elif flg == 1:
            ans = 0
            if masu[p][q] == "#":
                ans -= 1
            ans = ans + sum_row[p] + sum_column[q]

            print(ans)


if __name__ == '__main__':
    main()