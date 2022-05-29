def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    # 処理
    zahyo = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'o':
                zahyo.append([i, j])

    kyori = abs(zahyo[0][0] - zahyo[1][0]) + abs(zahyo[0][1] - zahyo[1][1])
    
    # 答えを出力
    print(kyori)


if __name__ == '__main__':
    main()