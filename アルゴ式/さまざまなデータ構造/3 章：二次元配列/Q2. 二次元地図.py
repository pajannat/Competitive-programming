def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())

    grid = [[0]*W for _ in range(H)]
    for h in range(H):
        S = input().rstrip()
        for w in range(W):
            if S[w] == "#":
                grid[h][w] = 1
            else:
                grid[h][w] = 0
    
    p, q = map(int, input().split())

    # 処理
    cnt = 0
    for i in range(W):
        cnt += grid[p][i]

    for i in range(H):
        cnt += grid[i][q]

    cnt -= grid[p][q]
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()