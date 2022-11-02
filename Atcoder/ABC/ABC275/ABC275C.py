def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    S = []
    for _ in range(9):
        S.append(list(input().rstrip()))
    zahyo = []
    cnt = 0
    
    # 処理
    # ポーンが置かれている座標を取得する
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                zahyo.append([i+1, j+1])
    
    # ポーンが置かれている座標4点を選ぶ
    # 選び方を全探索する
    for i in range(len(zahyo)):
        for j in range(i+1, len(zahyo)):
            for k in range(j+1, len(zahyo)):
                for l in range(k+1, len(zahyo)):
                    D1 = ((zahyo[i][0]-zahyo[j][0])**2 + (zahyo[i][1]-zahyo[j][1])**2)
                    D2 = ((zahyo[i][0]-zahyo[k][0])**2 + (zahyo[i][1]-zahyo[k][1])**2)
                    D3 = ((zahyo[i][0]-zahyo[l][0])**2 + (zahyo[i][1]-zahyo[l][1])**2)
                    D4 = ((zahyo[j][0]-zahyo[k][0])**2 + (zahyo[j][1]-zahyo[k][1])**2)
                    D5 = ((zahyo[j][0]-zahyo[l][0])**2 + (zahyo[j][1]-zahyo[l][1])**2)
                    D6 = ((zahyo[k][0]-zahyo[l][0])**2 + (zahyo[k][1]-zahyo[l][1])**2)
                    D = [D1, D2, D3, D4, D5, D6]
                    D.sort()
                    d1, d2, d3, d4, d5, d6 = D

                    if (d1 == d2 == d3 == d4) and (d5 == d6) and (d5 == 2*d1):
                        cnt += 1
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()