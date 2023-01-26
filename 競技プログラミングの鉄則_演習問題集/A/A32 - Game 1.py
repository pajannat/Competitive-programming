def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, A, B = map(int, input().split())
    first_win = [None] * (N + 1)

    # 処理
    for i in range(N+1):
        # 先手がA, B個を1回も取れない場合
        if i < A:
            first_win[i] = False
            continue
        # 先手がA, B個取り除くと、後手が1回も取れなくなる場合
        elif i < A+B:
            first_win[i] = True
            continue

        # 先手でA, B個どちらの個数でも取り除いて、後手を負けの状態にできるとき
        if first_win[i-A] == False or first_win[i-B] == False:
            first_win[i] = True
        # それ以外
        else:
            first_win[i] = False

    
    # 答えを出力
    if first_win[N]:
        print("First")
    else:
        print("Second")


if __name__ == '__main__':
    main()