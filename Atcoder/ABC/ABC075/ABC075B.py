def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    masu = [list(input().rstrip()) for _ in range(H)]
    masu_cnt = [[0]*W for _ in range(H)]
    search = [[1,1], [1,0], [0,1], [-1,0], [0,-1], [1,-1], [-1,1], [-1,-1]]

    # 処理
    for h in range(H):
        for w in range(W):
            # masu[h][w]が爆弾マスの場合
            if masu[h][w] == "#":
                masu_cnt[h][w] = "#"
                continue

            cnt = 0

            # masu[h][w]の周囲のマスの爆弾の数を数える
            for vec in search:
                h_vec, w_vec = vec
                h_idx = h + h_vec
                w_idx = w + w_vec

                # masu[h_idx][w_idx]マスが範囲内であれば処理
                if (0 <= h_idx < H) and (0 <= w_idx < W):
                    # masu[h_idx][w_idx]マスが爆弾であればカウント
                    if masu[h_idx][w_idx] == "#":
                        cnt += 1

            masu_cnt[h][w] = str(cnt)
    
    # 答えを出力
    for S in masu_cnt:
        print(''.join(S))


if __name__ == '__main__':
    main()