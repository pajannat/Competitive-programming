def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B, K = map(int, input().split())

    # 処理
    tmp = A
    cnt = 0
    for i in range(100):
        if tmp >= B:
            break
        cnt += 1
        tmp *= K
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()