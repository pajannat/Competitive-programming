def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())
    nex_list = [-1 for _ in range(N)]
    bak_list = [-1 for _ in range(N)]
    
    # クエリ処理
    for _ in range(Q):
        query = list(map(int, input().split()))

        flg = query[0]

        # Connect query
        if flg == 0:
            p, q = query[1], query[2]
            nex_list[p] = q
            bak_list[q] = p

        # Contract query
        if flg == 1:
            r = query[1]
            # rの前をrの後ろに連結
            nex_list[bak_list[r]] = nex_list[r]
            # rの次をrの前に連結
            bak_list[nex_list[r]] = bak_list[r]
            # rの連結を解除
            nex_list[r] = -1
            bak_list[r] = -1

    cnt = 0
    # 車両0の後方に連結する列車の数をカウント
    nex_train = nex_list[0]
    while True:
        if nex_train == -1:
            break
        else:
            cnt += 1
            nex_train = nex_list[nex_train]

    # 車両0の前方に連結する列車の数をカウント
    bak_train = bak_list[0]
    while True:
        if bak_train == -1:
            break
        else:
            cnt += 1
            bak_train = bak_list[bak_train]

    # 車両0をカウント
    cnt += 1

    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()