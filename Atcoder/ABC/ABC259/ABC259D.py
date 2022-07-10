def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())

    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append([x, y, r])

    # 処理

    # (sx, sy), (tx, ty) がどの円周上にあるか特定する
    s_circle_idx = -1
    t_circle_idx = -1
    for i, circle in enumerate(circles):
        x, y, r = circle[0], circle[1], circle[2]
        kyori_s = (sx-x)**2 + (sy-y)**2
        kyori_t = (tx-x)**2 + (ty-y)**2
        if kyori_s == r**2:
            s_circle_idx = i
        if kyori_t == r**2:
            t_circle_idx = i
    
    # 各circleからどこのcircleにいけるかの無向グラフを作成
    G = [[] for i in range(N)]

    for i, circle in enumerate(circles):
        xi, yi, ri = circle[0], circle[1], circle[2]

        for j, circle in enumerate(circles):
            xj, yj, rj = circle[0], circle[1], circle[2]

            # i == j はスキップ
            if i == j:
                continue

            kyori = (xi-xj)**2 + (yi-yj)**2
            if kyori <= (ri + rj)**2 and kyori >= (ri-rj)**2:
                # 頂点 i から頂点 j への辺を張る
                G[i].append(j)

    # s_circleからt_circleへ到達可能かグラフを探索
    flg = False

    # s, t が同一円周上にある場合は到達可能
    if s_circle_idx == t_circle_idx:
        flg = True

    # sからtへ到達可能かグラフを幅優先探索
    from collections import deque
    dist = [-1] * (N)
    dist[s_circle_idx] = 0

    d = deque()
    d.append(s_circle_idx)

    while d:
        v = d.popleft()
        for i in G[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
    
    # sからtへ到達していた場合はTrue
    if dist[t_circle_idx] != -1:
        flg = True
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()