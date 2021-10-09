def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    # sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(n, l, r):
        if n > r-l+1:
            return []
        if n == 0:
            return [[]]

        # 答えを格納する配列 ans を用意する。
        ans = []

        # func(n-1, l+1, r) の返却する配列について、
        # それぞれの要素の頭に l をつけたものを ans に格納する。
        for ret in func(n-1, l+1, r):
            ret.insert(0, l)
            ans.append(ret)

        # func(n, l+1, r) の返却する配列について、
        # それぞれの要素を ans に格納する。
        for ret in func(n, l+1, r):
            ans.append(ret)

        return ans

    # 入力
    N, L, R = map(int, input().split())

    # 出力
    print(len(func(N, L, R)))

if __name__ == '__main__':
    main()