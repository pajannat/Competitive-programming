def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    heap = []

    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            v = int(query[1])

            # キー v をもつ頂点をヒープの最後尾に挿入
            heap.append(v)
            idx = len(heap) - 1
            parent_idx = (idx - 1) // 2

            # swapを繰り返す
            # idx == 0 (根に到達)で処理を終了
            while idx > 0:
                # 頂点と親の頂点とがヒープ条件を満たすならば処理を終了
                if heap[parent_idx] >= heap[idx]:
                    break
                #  ヒープ条件を満たさない場合は、挿入した頂点と親の頂点を swap
                else:
                    heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                    idx = parent_idx
                    parent_idx = (idx - 1) // 2

        # Pop query
        elif flg == 1:
            # 根を削除. heap配列の末尾の項を根に持ってくる.
            heap[0], heap[-1] = heap[-1], heap[0]
            # 最大値をpop
            print(heap.pop(-1))

            # ヒープ条件を満たすまで、根に持ってきた要素とその子頂点と swap
            idx = 0
            child1 = (idx*2 + 1)
            # child1 + 1 が配列のidxの範囲を超える場合
            if child1 + 1 > len(heap) - 1:
                child2 = child1
            # child1 + 1 が配列のidxの範囲を超えない場合
            else:
                child2 = child1 + 1

            # 子頂点が存在する間, 処理を続ける
            while child1 <= (len(heap) - 1):
                # ヒープ条件を満たす場合は処理を終了
                if (heap[idx] >= heap[child1]) and (heap[idx] >= heap[child2]):
                    break

                else:
                    # swap する子頂点は、キーが大きい方を選択
                    # 左右の子頂点のキーが等しい場合は左側を選択
                    if heap[child1] >= heap[child2]:
                        max_child_idx = child1
                    else:
                        max_child_idx = child2
                    
                    # swap処理
                    heap[idx], heap[max_child_idx] = heap[max_child_idx], heap[idx]
                    # idxを更新
                    idx = max_child_idx

                    child1 = (idx*2 + 1)

                    # child1 + 1 が配列のidxの範囲を超える場合
                    if child1 + 1 > len(heap) - 1:
                        child2 = child1
                    # child1 + 1 が配列のidxの範囲を超えない場合
                    else:
                        child2 = child1 + 1


if __name__ == '__main__':
    main()