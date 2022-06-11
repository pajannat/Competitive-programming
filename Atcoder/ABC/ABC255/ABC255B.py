def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY_light_len = [10000000 for _ in range(N)]

    # 処理
    for i, XandY in enumerate(XY):
        x, y = XandY[0], XandY[1]
        for a in A:
            j = a-1
            X, Y = XY[j][0], XY[j][1]
            kyori = ((X-x)**2 + (Y-y)**2)**(1/2)
            # print(x, y, X, Y, kyori)
            if kyori == 0:
                pass
            else:
                XY_light_len[i] = min(kyori, XY_light_len[i])
    
    ans = -1
    for i in range(N):
        if i+1 in A:
            pass
        else:
            ans = max(ans, XY_light_len[i])
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()