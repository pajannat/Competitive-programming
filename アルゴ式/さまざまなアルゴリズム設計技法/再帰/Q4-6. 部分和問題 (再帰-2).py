def main():
    from sys import stdin
    input = stdin.readline

    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+7))

    # 再帰関数
    def func(i, j):
        # 終了条件
        if i == 0:
            if j == 0:
                return 1
            else:
                return 0
        else:
            flg = 0
            # A[i-1]を選ぶ場合
            if j >= A[i-1]:
                # func(i-1, j-A[i-1])が探索済みの場合
                if memo[i-1][j-A[i-1]] != -1:
                    flg = memo[i-1][j-A[i-1]]
                # func(i-1, j-A[i-1])が未探索の場合
                # func(i-1, j-A[i-1])を呼び出し計算する
                else:
                    flg = func(i-1, j-A[i-1])

            # A[i-1]を選ぶ場合でflg = 1となっていない場合
            if flg == 0:
                # A[i-1]を選ばない場合
                # func(i-1, j)が探索済みの場合
                if memo[i-1][j] != -1:
                    flg = memo[i-1][j]
                # func(i-1, j)が未探索の場合
                # func(i-1, j)を呼び出し計算する
                else:
                    flg = func(i-1, j)

            # func(i, j)の計算結果をmemo[i][j]に格納
            memo[i][j] = flg
        return flg

    # 入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # memo[i][j] == -1 はfunc(i, j)が未探索であることを示す。
    memo = [[-1]*(X+1) for _ in range(N+1)]
    memo[0][0] = 1

    # 出力
    if func(N, X) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()