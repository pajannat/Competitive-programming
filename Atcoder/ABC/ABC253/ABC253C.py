def main():
    from sys import stdin
    input = stdin.readline

    import heapq

    # 入力を受け取る
    Q = int(input())
    S_max = []
    S_min = []
    heapq.heapify(S_max)
    heapq.heapify(S_min)
    S_x_count = {}

    # 答えを出力
    for _ in range(Q):
        query = list(map(int, input().split()))
        # append query
        if query[0] == 1:
            x = query[1]
            heapq.heappush(S_max, -x)
            heapq.heappush(S_min, x)
            if x not in S_x_count.keys():
                S_x_count[x] = 1
            else:
                S_x_count[x] += 1

        # erase query
        if query[0] == 2:
            x = query[1]
            c = query[2]
            # S から x を min(c, (S に含まれる x の個数 )) 個削除
            if x not in S_x_count.keys():
                pass
            else:
                S_x_count[x] -= min(x, c)
                if S_x_count[x] == 0:
                    S_x_count.pop(x)

        # print query
        if query[0] == 3:
            # (S の最大値 )− (S の最小値 ) を出力
            # 最小値の取得
            min_value = 10**9 + 1
            for _ in range(10**6):
                if S_min[0] in S_x_count.keys():
                    min_value = S_min[0]
                    break
                else:
                    heapq.heappop(S_min)

            # 最大値の取得
            max_value = -1
            for _ in range(10**6):
                if -S_max[0] in S_x_count.keys():
                    max_value = -S_max[0]
                    break
                else:
                    heapq.heappop(S_max)
            
            # (S の最大値 )− (S の最小値 ) を出力
            print(max_value - min_value)


if __name__ == '__main__':
    main()