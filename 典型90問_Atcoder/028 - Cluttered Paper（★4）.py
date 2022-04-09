def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 領域加算は二次元いもす法
    m = 1010
    imos = [[0 for j in range(m)] for i in range(m)]

    # imos[x][y] += 1は(x,y),(x+1,y+1)で囲われる領域に1加算とする
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        imos[lx][ly] += 1
        imos[rx][ry] += 1
        imos[rx][ly] -= 1
        imos[lx][ry] -= 1
    
    # いもす法の処理
    # 今回のimos[x][y] += 1の定義により 0 <= i <= m-1, 0 <= j <= m-1
    # x軸の正方向に累積和
    for i in range(m-1):
        for j in range(m-1):
            imos[i][j+1] += imos[i][j]
    
    # y軸の正方向に累積和
    for i in range(m-1):
        for j in range(m-1):
            imos[i+1][j] += imos[i][j]
    
    # 重なりが0~Nの領域はそれぞれいくつあるか?
    # imosを全探索してそれぞれカウント
    ans = [0 for i in range(N+1)]

    for i in range(m):
        for j in range(m):
            ans[imos[i][j]] += 1
    
    # 答えを出力
    for i in range(1, N+1):
        print(ans[i])
    
if __name__ == '__main__':
    main()