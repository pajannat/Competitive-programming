def main():
    from sys import stdin
    input = stdin.readline

    import numpy as np

    # 入力を受け取る
    S = []
    for _ in range(9):
        S.append(list(input().rstrip()))
    zahyo = []
    senbun = []
    cnt = 0
    
    # 処理
    # ポーンが置かれている座標を取得する
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                zahyo.append([i+1, j+1])
    
    # ポーンが置かれている2点を結ぶ線分を列挙する
    # [[座標1], [座標2], 線分の長さ]
    for i in range(len(zahyo)):
        for j in range(i+1, len(zahyo)):
            nagasa = ((zahyo[i][0] - zahyo[j][0])**2 + (zahyo[i][1] - zahyo[j][1])**2 ) ** 0.5
            senbun.append([zahyo[i], zahyo[j], nagasa])

    # 線分 A, B を選ぶ組み合わせを全探索
        # 内積 == 0
        # 外積 < 0
        # Aの長さ == Bの長さ
        # をすべて満たすとき cnt += 1
    for i in range(len(senbun)):
        for j in range(i+1, len(senbun)):
            # ok_flg が 1のままであればok
            ok_flg = 1
            AB = np.array([senbun[i][:2][0][0] - senbun[i][:2][1][0], senbun[i][:2][0][1] - senbun[i][:2][1][1]])
            CD = np.array([senbun[j][:2][0][0] - senbun[j][:2][1][0], senbun[j][:2][0][1] - senbun[j][:2][1][1]])
            AC = np.array([senbun[j][:2][1][0] - senbun[i][:2][1][0], senbun[j][:2][1][1] - senbun[i][:2][1][1]])
            AD = np.array([senbun[j][:2][0][0] - senbun[i][:2][1][0], senbun[j][:2][0][1] - senbun[i][:2][1][1]])

            a1xy = (senbun[i][:2][0][0], senbun[i][:2][0][1])
            a2xy = (senbun[i][:2][1][0], senbun[i][:2][1][1])
            b1xy = (senbun[j][:2][0][0], senbun[j][:2][0][1])
            b2xy = (senbun[j][:2][1][0], senbun[j][:2][1][1])

            # 内積 == 0 か?
            if AB@CD != 0:
                ok_flg = 0
            
            # 外積(|AB × AC|) * (|AB × AD|) < 0 か?
            if np.cross(AB, AC)*np.cross(AB, AD) >= 0:
                ok_flg = 0
            
            # Aの長さ == Bの長さ か?
            if senbun[i][2] != senbun[j][2]:
                ok_flg = 0
            
            # 同じ頂点を持っているか?
            if a1xy in [b1xy, b2xy] or a2xy in [b1xy, b2xy]:
                ok_flg = 0
            
            if ok_flg == 1:
                cnt += 1
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()