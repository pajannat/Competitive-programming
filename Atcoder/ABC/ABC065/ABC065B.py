def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = [-1] * (10**5 + 1)
    for i in range(1, N+1):
        A[i] = int(input())

    light_num = 1
    cnt = 0

    # 処理
    while True:
        # 光っているボタン i を押す
        # ボタン Ai に明かりを付ける
        light_num = A[light_num]

        cnt += 1

        # ボタン 2 が光ったら cntを出力
        if light_num == 2:
            print(cnt)
            exit()

        # cnt >= (10**5 + 1) なら -1 を出力
        if cnt > 10**5:
            print(-1)
            exit()


if __name__ == '__main__':
    main()