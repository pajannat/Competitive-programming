def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 数列に含まれる整数 xの数を管理
    counter = [0 for _ in range(100001)]

    # 初期状態の数列に含まれる整数 xの数をカウント
    for a in A:
        counter[a] += 1

    sum_A = sum(A)

    # 処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            v = int(query[1])
            counter[v] += 1
            sum_A += v

        # Change query
        elif flg == 1:
            x, y = int(query[1]), int(query[2])
            cnt_x = counter[x]
            cnt_y = counter[y]
            # 数列に含まれる整数 x, yの数を修正
            counter[x] = 0
            counter[y] += cnt_x
            # 数列の合計値を修正
            sum_A = sum_A - x*cnt_x + y*cnt_x

        # Sum query
        elif flg == 2:
            print(sum_A)


if __name__ == '__main__':
    main()