def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    table = [[0]*N for i in range(N)]

    # 処理
    for i in range(N):
        A = input().rstrip()
        for j in range(N):
            result = A[j]

            if result == "W":
                table[i][j] = 1
            elif result == "L":
                table[i][j] = 2
            elif result == "D":
                table[i][j] = 3
            else:
                pass
    
    flg = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if (table[i][j] == 1) and (table[j][i] != 2):
                flg = False

            if (table[i][j] == 2) and (table[j][i] != 1):
                flg = False

            if (table[i][j] == 3) and (table[j][i] != 3):
                flg = False
    
    # 答えを出力
    if flg:
        print("correct")
    else:
        print("incorrect")


if __name__ == '__main__':
    main()