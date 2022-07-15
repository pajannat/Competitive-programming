def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    masu = [list(input().rstrip()) for _ in range(H)]

    # 上下左右への移動
    idou = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    Q = int(input())
    for _ in range(Q):
        # クエリを受け取る
        x, y = map(int, input().split())

        # x, y の周り(上下左右)の爆弾の数 cnt を初期化
        cnt = 0

        # x, y の周り(上下左右)の爆弾の数 cnt をカウント
        for x_y in idou:
            plus_x, plus_y = x_y[0], x_y[1]
            # 調べるマス (X, Y)
            X = x + plus_x
            Y = y + plus_y
            # マス(X, Y) に爆弾があれば cnt += 1
            # マス(X, Y) が範囲外である場合はスキップ
            if 0 <= X <= H-1 and 0 <= Y <= W-1:
                if masu[X][Y] == "#":
                    cnt += 1

        # x, y の周り(上下左右)の爆弾の数 cnt を出力
        print(cnt)


if __name__ == '__main__':
    main()