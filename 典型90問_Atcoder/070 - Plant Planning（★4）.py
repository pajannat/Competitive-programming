def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    X_list = []
    Y_list = []

    for _ in range(N):
        X, Y = map(int, input().split())
        X_list.append(X)
        Y_list.append(Y)

    # 処理
    # X, Y座標をソート
    X_list.sort()
    Y_list.sort()

    # X, Y座標別々にマンハッタン距離最小となる点を求める
    # 中央値がマンハッタン距離最小となる点
    X_median = 0
    if len(X_list) % 2 == 0:
        X_median = (X_list[len(X_list)//2] + X_list[len(X_list)//2 -1]) / 2
    else:
        X_median = X_list[len(X_list)//2]

    Y_median = 0
    if len(Y_list) % 2 == 0:
        Y_median = (Y_list[len(Y_list)//2] + Y_list[len(Y_list)//2 - 1]) / 2
    else:
        Y_median = Y_list[len(Y_list)//2]
    
    ans = 0
    for x, y in zip(X_list, Y_list):
        ans += abs(x - X_median)
        ans += abs(y - Y_median)
    
    # 今回の制約ではansは整数となる。答えの形式に合わせ変数をint型へ変換
    ans = int(ans)
    
    # 答えを出力
    print(int(ans))


if __name__ == '__main__':
    main()