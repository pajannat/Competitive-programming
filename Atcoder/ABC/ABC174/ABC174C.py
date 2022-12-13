def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    K = int(input())
    cnt = 0
    a = 0
    b = 7

    a = (a + b) % K
    cnt += 1

    # 処理
    for i in range(1, 10**6 + 10):
        if a == 0:
            break

        # 計算1回ごとに mod K を取ることで数が大きくなりすぎないようにする
        b = (b*10) % K
        a = (a + b) % K
        cnt += 1
    
    # 答えを出力
    if cnt > 10**6:
        print(-1)
    else:
        print(cnt)


if __name__ == '__main__':
    main()