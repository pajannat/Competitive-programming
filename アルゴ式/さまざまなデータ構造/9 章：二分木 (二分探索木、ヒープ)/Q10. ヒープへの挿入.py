def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    heap = []

    Q = int(input())
    for _ in range(Q):
        v = int(input())

        # キー v をもつ頂点をヒープの最後尾に挿入
        heap.append(v)
        idx = len(heap) - 1
        parent_idx = (idx - 1) // 2

        # swapを繰り返す
        while True:
            # 頂点と親の頂点とがヒープ条件を満たすならば処理を終了
            if heap[parent_idx] >= heap[idx]:
                break
            #  ヒープ条件を満たさない場合は、挿入した頂点と親の頂点を swap
            else:
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx
                parent_idx = (idx - 1) // 2
                # idx == 0 (根に到達)でも処理を終了
                if idx == 0:
                    break
    
    # 答えを出力
    print(*heap)


if __name__ == '__main__':
    main()