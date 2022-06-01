def main():
    from sys import stdin
    input = stdin.readline
    
    # 入力を受け取る
    H, W = map(int, input().split())

    grid = [[0]*W for _ in range(H)]
    for h in range(H):
        S = input().rstrip()
        for w, s in enumerate(S):
            if s == "#":
                grid[h][w] = 1
            else:
                grid[h][w] = 0

    # 前処理
    H_sum = [0]*H
    W_sum = [0]*W
    for h in range(H):
        cnt = 0
        for w in range(W):
            cnt += grid[h][w]
        H_sum[h] = cnt

    for w in range(W):
        cnt = 0
        for h in range(H):
            cnt += grid[h][w]
        W_sum[w] = cnt

    # クエリに答える
    Q = int(input())
    for _ in range(Q):
        p, q = map(int, input().split())

        # 処理
        ans = H_sum[p] + W_sum[q] - grid[p][q]
        
        # 答えを出力
        print(ans)


if __name__ == '__main__':
    main()