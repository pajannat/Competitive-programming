def main():
    from sys import stdin
    input = stdin.readline

    import random

    def GetDistance(idx1, idx2):
        dist = ( (XY[idx1][0]-XY[idx2][0])**2 + (XY[idx1][1]-XY[idx2][1])**2 )**0.5
        return dist
    
    def GetScore(P, XY):
        sum = 0
        for i in range(len(P)-1):
            sum += GetDistance(P[i]-1, P[i+1]-1)
        return sum


    # 入力を受け取る
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    # 初期解を設定
    P = [i for i in range(1, N+1)] + [1]
    score = 0
    # 探索回数
    search_num = 5 * 10 ** 4
 
    # 処理
    # 初期解のスコアを計算
    score = GetScore(P, XY)
    # print(score)

    # 山登り法
    for i in range(search_num):
        L, R = random.sample(range(1, len(P)), 2)
        if R < L:
            L, R = R, L

        # 巡回順序を部分的に反転
        P_LR = P[L:R][::-1]
        tmp_P = P[:L] + P_LR + P[R:]

        # score を計算して、改善したら P を更新
        tmp_score = GetScore(tmp_P, XY)
        if tmp_score < score:
            score = tmp_score
            P = tmp_P
            # print(score)
        

    # 答えを出力
    for p in P:
        print(p)


if __name__ == '__main__':
    main()