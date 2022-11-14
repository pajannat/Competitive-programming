def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict, deque

    # 入力を受け取る
    N = int(input())
    graph = defaultdict(list)

    # 処理
    for _ in range(N):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    
    que = deque()
    # 探索元として頂点 1 を追加
    que.append(1)
    # 到達した階層をSに記録
    S = {1}

    # 階層1 から到達可能な階層を探索
    # que に要素が入っている限り, 繰り返す
    while que:
        # 階層v から到達可能な階層を探索
        v = que.popleft()
        # v から移動可能な階層 i を探索
        for i in graph[v]:
            # i へ移動するのが初めての場合
            if not i in S:
                # 階層i から到達可能な階層はまだ未探索
                # 探索開始点として i をqueに追加
                que.append(i)
                # 到達した階層としてSに記録
                S.add(i)
    
    # 答えを出力
    # 到達した階層の最大値を出力
    print(max(S))


if __name__ == '__main__':
    main()