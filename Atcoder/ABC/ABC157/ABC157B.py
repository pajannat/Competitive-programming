def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    punched = [[0]*3 for _ in range(3)]
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    for _ in range(N):
        num = int(input())
        # ビンゴカードに穴を開ける
        for i in range(3):
            for j in range(3):
                if num == A[i][j]:
                    punched[i][j] = 1

    # 処理
    # 縦方向に揃っているかチェック
    for i in range(3):
        cnt = 0
        for j in range(3):
            cnt += punched[i][j]
        if cnt == 3:
            print("Yes")
            exit()

    # 横方向に揃っているかチェック
    for i in range(3):
        cnt = 0
        for j in range(3):
            cnt += punched[j][i]
        if cnt == 3:
            print("Yes")
            exit()
    
    # 斜め方向に揃っているかチェック
    if (punched[0][0]==1) and (punched[1][1]==1) and (punched[2][2]==1):
        print("Yes")
        exit()
    
    if (punched[0][2]==1) and (punched[1][1]==1) and (punched[2][0]==1):
        print("Yes")
        exit()
    
    print("No")


if __name__ == '__main__':
    main()