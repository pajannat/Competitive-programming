def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]
    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)

    from collections import deque
    dist = [-1] * (N+1)

    d = deque()

    # 開始地点を頂点0から全探索
    for i in range(N):
        # 探索済みであればスキップ
        if dist[i] != -1:
            continue
        d.append(i)
        dist[i] = 0

        while d:
            v = d.popleft()
            for i in adj[v]:
                if dist[i] != -1:
                    continue
                dist[i] = dist[v] + 1
                d.append(i)

    # 二部グラフの判定
    flg = True
    for i, a in enumerate(adj):
        for j in a:
            # 辺の両端点が同色であればFalse
            if dist[i]%2 == dist[j]%2:
                flg = False
    
    # 答えを出力
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()