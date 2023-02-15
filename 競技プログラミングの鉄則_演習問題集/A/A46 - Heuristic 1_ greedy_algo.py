def main():
    from sys import stdin
    input = stdin.readline

    def GetDistance(idx1, idx2):
        dist = ( (XY[idx1][0]-XY[idx2][0])**2 + (XY[idx1][1]-XY[idx2][1])**2 )**0.5
        return dist

    # 入力を受け取る
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    score = 10**6
    sum_dist = 0

    used = [0] * N

    # 処理
    now_idx = 0
    used[0] = 1
    for i in range(N):
        print(now_idx+1)
        min_dist = 10000
        min_idx = now_idx

        for j in range(N):
            # j == now_idx のとき or j が使用済みの場合はスキップ
            if j == now_idx or used[j] == 1:
                continue

            # j, now_idx の距離を計算する
            dist = GetDistance(j, now_idx)
            if dist <= min_dist:
                min_dist = dist
                min_idx = j
        
        # 選択した idx を使用済みにする
        used[min_idx] = 1
        now_idx = min_idx

        # sum_dist に加算
        # 最後は idx: N-1 -> 0
        if i == N-1:
            sum_dist += GetDistance(0, now_idx)
            now_idx = 0
        else:
            sum_dist += min_dist
    
    print(now_idx+1)

    # # 答えを出力
    # score = score / sum_dist
    # print(sum_dist)
    # print(score)


if __name__ == '__main__':
    main()