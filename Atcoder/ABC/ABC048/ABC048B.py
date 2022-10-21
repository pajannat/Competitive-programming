def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    a, b, x = map(int, input().split())

    # 処理
    # 0 <= i <= a を満たす整数 i のうち
    # xで割り切れる iの個数をカウントする
    def f(a, x):
        if a == -1:
            return 0
        else:
            return (a // x) + 1
    
    # 答えを出力
    print(f(b, x) - f(a-1, x))


if __name__ == '__main__':
    main()