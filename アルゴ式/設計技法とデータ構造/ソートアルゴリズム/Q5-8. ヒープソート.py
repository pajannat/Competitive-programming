def main():
    from sys import stdin
    input = stdin.readline

    def f(list):
        N = len(list)
        x = (N // 2) - 1

        # x ≥0 を満たす間次の処理を繰り返し行う。
        while x >= 0:
            # k = x とおき、次の処理を繰り返し行う。
            k = x
            while True:
                # 頂点 k が子ノードを持たなければ処理を終了する。
                if (2*k+1 > N-1) and ((2*k+2 > N-1)):
                    break
                else:
                    # A[k], A[2k+1] (頂点 k の左側の子ノード),
                    #  (もし存在すれば) A[2k+2] (頂点 k の左側の子ノード) の値を比較し
                    # 最大値を持つノードを選択する。
                    # ただし、最大値を持つノードが複数ある場合は
                    # 頂点 k, 頂点 2k+1, 頂点 2k+2 の順に選択する。
                    if (2*k+2 <= N-1):
                        tmp = max(list[k], list[2*k+1], list[2*k+2])
                        # 頂点 k を選択した場合
                        if tmp == list[k]:
                        # 処理を終了する。
                            break
                        # 頂点 2k+1 を選択した場合
                        elif tmp == list[2*k+1]:
                            # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                            list[k], list[2*k+1] = list[2*k+1], list[k]
                            k = 2*k + 1
                        # 頂点 2k+2 を選択した場合
                        else:
                            # A[k] と A[2k+2] を入れ替え k の値を 2k+2 に更新する。
                            list[k], list[2*k+2] = list[2*k+2], list[k]
                            k = 2*k + 2               
                    else:
                        tmp = max(list[k], list[2*k+1])
                        # 頂点 k を選択した場合
                        if tmp == list[k]:
                        # 処理を終了する。
                            break
                        # 頂点 2k+1 を選択した場合
                        elif tmp == list[2*k+1]:
                            # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                            list[k], list[2*k+1] = list[2*k+1], list[k]
                            k = 2*k + 1

            # x の値を 1 だけ減らす。
            x -= 1
        return list

    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_heap = f(A)

    for i in range(N-1, 0, -1):
        A_heap[0], A_heap[i] = A_heap[i], A_heap[0]
        
        k = 0
        while True:
            # 頂点 k が子ノードを持たなければ処理を終了する。
            if (2*k+1 > i-1) and ((2*k+2 > i-1)):
                break
            else:
                if (2*k+2 <= i-1):
                    tmp = max(A_heap[k], A_heap[2*k+1], A_heap[2*k+2])
                    # 頂点 k を選択した場合
                    if tmp == A_heap[k]:
                    # 処理を終了する。
                        break
                    # 頂点 2k+1 を選択した場合
                    elif tmp == A_heap[2*k+1]:
                        # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                        A_heap[k], A_heap[2*k+1] = A_heap[2*k+1], A_heap[k]
                        k = 2*k + 1
                    # 頂点 2k+2 を選択した場合
                    else:
                        # A[k] と A[2k+2] を入れ替え k の値を 2k+2 に更新する。
                        A_heap[k], A_heap[2*k+2] = A_heap[2*k+2], A_heap[k]
                        k = 2*k + 2               
                else:
                    tmp = max(A_heap[k], A_heap[2*k+1])
                    # 頂点 k を選択した場合
                    if tmp == A_heap[k]:
                    # 処理を終了する。
                        break
                    # 頂点 2k+1 を選択した場合
                    elif tmp == A_heap[2*k+1]:
                        # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                        A_heap[k], A_heap[2*k+1] = A_heap[2*k+1], A_heap[k]
                        k = 2*k + 1
        
        if i == M:
            print(*A_heap)


    print(*A_heap)

if __name__ == '__main__':
    main()