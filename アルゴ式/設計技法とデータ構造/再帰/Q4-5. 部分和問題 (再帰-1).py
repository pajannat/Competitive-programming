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
                return True
            else:
                return False
        else:
            flg = False
            # A[i-1]を選ぶ場合
            if (j >= A[i-1]) and (func(i-1, j-A[i-1]) == True):
                flg = True
            
            # A[i-1]を選ばない場合
            if func(i-1, j) == True:
                flg = True

        return flg

    # 入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    flg = False

    # 出力
    if func(N, X):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()