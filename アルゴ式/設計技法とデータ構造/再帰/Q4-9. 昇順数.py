def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+5))

    # 再帰関数(Q4-7. 数を選ぶ (1))
    def func(n, l, r):
        # もし l > r ならば、空配列を返却する。
        if l > r:
            return []

        # もし n = 0 ならば、空配列の入った配列を返却する。
        if n == 0:
            return [[]]

        # 答えを格納する配列 ans を用意する。
        ans = []

        # func(n-1, l, r) の返却する配列について、
        # それぞれの要素の頭に l をつけたものを ans に格納する。
        for ret in func(n-1, l, r):
            ret.insert(0, l)
            ans.append(ret)

        # func(n, l+1, r) の返却する配列について、
        # それぞれの要素を ans に格納する。
        for ret in func(n, l+1, r):
            ans.append(ret)

        return ans

    # 入力
    L, R = map(int, input().split())

    n = len(str(L))
    l = 1
    r = 9

    ans = 0
    for n in range(len(str(L)), len(str(R))+1):
        # 再帰関数funcを用いて、桁数l~rの昇順数を列挙
        # L以上R以下の昇順数をansに加算
        for list in func(n, l, r):
            num = int(''.join(map(str, list)))
            if L <= num <= R:
                ans += num

    # 出力
    print(ans)

if __name__ == '__main__':
    main()