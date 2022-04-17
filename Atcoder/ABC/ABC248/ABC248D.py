def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 処理
    place = [[]*(N+1) for i in range(N+1)]

    for i, a in enumerate(A):
        # 数値aがどこ(i)で出現したかを記録
        place[a].append(i+1)

    # クエリ処理
    import bisect
    for i in range(Q):
        L, R, X = map(int, input().split())
        # 数値Xがidx Lの一つ前までに何回出現しているか
        L_cnt = bisect.bisect_right(place[X], L-1)
        # 数値Xがidx Rまでに何回出現しているか
        R_cnt = bisect.bisect_right(place[X], R)
        # 答えを出力
        print(R_cnt - L_cnt)


if __name__ == '__main__':
    main()