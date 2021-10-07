def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(A, B):
        # 終了条件
        if B == A:
            return A

        # 再帰呼び出し
        return func(A, B-1) + B

    # 入力
    A, B = map(int, input().split())

    # 出力
    print(func(A, B))

if __name__ == '__main__':
    main()