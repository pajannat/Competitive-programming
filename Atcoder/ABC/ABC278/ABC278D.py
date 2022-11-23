def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # A[i] に加算された値を保持する
    d = defaultdict(lambda: 0)
    tmp_x = -1

    # 処理
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            xq = query[1]

            tmp_x = query[1]
            # すべての値がtmp_xとなるため、A[i]の加算値をclear
            d.clear()
        elif query[0] == 2:
            iq = query[1]
            xq = query[2]

            d[iq] += xq
        elif query[0] == 3:
            iq = query[1]

            # クエリ1が一度も実行されていない場合
            if tmp_x == -1:
                print(A[iq-1] + d[iq])
            # クエリ1が1回以上実行されている場合
            else:
                print(tmp_x + d[iq])


if __name__ == '__main__':
    main()