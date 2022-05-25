def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # ループの終了条件を管理するflg
    flg = True
    while flg:
        # ソート一周のうち、一度も更新されなければ
        # flg = Falseのままとなりループ終了
        flg = False
        for i in range(N-1):
            if A[i] > A[i+1]:
                # ソートが実行されるのでflg更新してループ継続
                flg = True
                # A[i]とA[i+1]の値の入れ替え
                A[i], A[i+1] = A[i+1], A[i]
        # ソート過程を出力
        if flg:
            print(*A)

if __name__ == '__main__':
    main()