def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    # R行 × C列の迷路
    R, C = map(int, input().split())

    # 迷路を格納
    maze = []
    for r in range(R):
        s = input().rstrip()
        maze.append(s)

    # R行 × C列の迷路訪問リストを用意
    cnt = [[0]*C for _ in range(R)]

    # 初期化
    cnt[0][0] = 1

    for i in range(R):
        for j in range(C):
            if maze[i][j] == '#':
                continue
            # 左からもらう場合
            if j >= 1:
                cnt[i][j] += cnt[i][j-1]
            # 上からもらう場合
            if i >= 1:
                cnt[i][j] += cnt[i-1][j]


    # 答えを出力
    print(cnt[R-1][C-1])


if __name__ == '__main__':
    main()