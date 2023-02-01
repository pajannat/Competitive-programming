def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    # 処理
    LR.sort(key=lambda x: x[1])
    R = LR[0][1]
    cnt = 1
    for i in range(1, N):
        now_L = LR[i][0]
        if R <= now_L:
            R = LR[i][1]
            cnt += 1
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()