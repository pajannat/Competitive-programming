def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    L1, R1, L2, R2 = map(int, input().split())
    counter = [0 for i in range(101)]

    # 処理
    for i in range(L1, R1):
        counter[i] += 1

    for i in range(L2, R2):
        counter[i] += 1
    
    cnt = 0
    for c in counter:
        if c == 2:
            cnt += 1
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()