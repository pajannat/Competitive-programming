def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    import heapq
    ToDo_heap = []

    Q = int(input())
    for i in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            t, S = int(query[1]), query[2]

            # ToDo_heap に t, i, S を挿入する
            # iは挿入順を意味する. 優先度が同じときの判断に使う.
            heapq.heappush(ToDo_heap, [t, i, S])


        # Pop query
        elif flg == 1:
            # ToDo_heap の締め切りが近いタスクを消化する
            # 該当するタスクが複数ある場合は、最も古くセットされたものを消化
            ans = heapq.heappop(ToDo_heap)
            # 答えを出力
            print(ans[2])


if __name__ == '__main__':
    main()