def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())

    # 処理
    def origin_calc(x):
        y = 0
        for s in str(x):
            y += int(s)
        z = (x + y) % 10**5
        return z
    
    vis = [-1] * 10**5
    vis[N] = 0
    break_x = N
    cnt = 0
    for _ in range(K):
        break_x = origin_calc(break_x)
        cnt += 1
        # 計算を繰り返し、一周して同じ数字になったとき
        if vis[break_x] != -1:
            # ループから抜ける
            break
        # まだ一周していない場合
        else:
            # 計算回数を記録
            vis[break_x] = cnt

    # ansを求めるための計算回数ans_cnt
    ans_cnt = cnt

    # 計算が一周してループを抜けた場合
    if K > cnt:
        # 周期T   N:0回 -> break_x:vis[break_x]回 -> break_x:cnt回
        T = cnt - vis[break_x]

        # ansを求めるための計算回数ans_cnt
        # break_xに初回到達までの回数 + (K - break_xに初回到達までの回数) % T
        ans_cnt = vis[break_x] + (K - vis[break_x]) % T
    
    ans = N
    for _ in range(ans_cnt):
        ans = origin_calc(ans)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()