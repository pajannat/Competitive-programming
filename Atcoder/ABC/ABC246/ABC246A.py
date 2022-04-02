def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    X_cnt = [0]*201
    Y_cnt = [0]*201

    # 処理
    for i in range(3):
        X, Y = map(int, input().split())
        X_idx = X + 100
        Y_idx = Y + 100
        X_cnt[X_idx] += 1
        Y_cnt[Y_idx] += 1

    X_ans = 0
    Y_ans = 0
    for i in range(201):
        if X_cnt[i] == 1:
            X_ans = i - 100
        if Y_cnt[i] == 1:
            Y_ans = i - 100
        
    # 答えを出力
    print(X_ans, Y_ans)

if __name__ == '__main__':
    main()