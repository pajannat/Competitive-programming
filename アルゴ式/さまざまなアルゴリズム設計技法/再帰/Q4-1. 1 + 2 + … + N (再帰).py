def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(x):
        # 終了条件
        if x == 0:
            return 0

        # 再帰呼び出し
        return func(x-1) + x

    # 入力
    N = int(input())

    # 出力
    print(func(N))

if __name__ == '__main__':
    main()