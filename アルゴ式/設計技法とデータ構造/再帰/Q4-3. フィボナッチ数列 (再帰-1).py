def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(N):
        # 終了条件
        if N == 0:
            return 0
        if N == 1:
            return 1

        # 再帰呼び出し
        return func(N-1) + func(N-2)

    # 入力
    N = int(input())

    # 出力
    print(func(N))

if __name__ == '__main__':
    main()