def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(N):
        # 終了条件
        if fib[N] != -1:
            return fib[N]
        else:
            fib[N] = func(N-1) + func(N-2)
            return fib[N]

        # 再帰呼び出し
        return fib[N]

    # 入力
    N = int(input())

    fib = [-1]*(N+1)
    fib[0] = 0
    fib[1] = 1

    # 出力
    print(func(N))

if __name__ == '__main__':
    main()