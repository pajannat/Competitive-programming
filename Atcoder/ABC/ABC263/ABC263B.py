def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    P = [-1, -1] + list(map(int, input().split()))

    # 処理

    cnt = 0
    # P_N から順に辿っていく
    i = N
    while True:
        # ループの先頭でカウント+1
        cnt += 1
        i = P[i]
    
        # P_i == 1 に到達したら終了
        if i == 1:
            break
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()