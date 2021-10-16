def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

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
                    tmp = max(A[k], A[2*k+1], A[2*k+2])
                    # 頂点 k を選択した場合
                    if tmp == A[k]:
                    # 処理を終了する。
                        break
                    # 頂点 2k+1 を選択した場合
                    elif tmp == A[2*k+1]:
                        # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                        A[k], A[2*k+1] = A[2*k+1], A[k]
                        k = 2*k + 1
                    # 頂点 2k+2 を選択した場合
                    else:
                        # A[k] と A[2k+2] を入れ替え k の値を 2k+2 に更新する。
                        A[k], A[2*k+2] = A[2*k+2], A[k]
                        k = 2*k + 2               
                else:
                    tmp = max(A[k], A[2*k+1])
                    # 頂点 k を選択した場合
                    if tmp == A[k]:
                    # 処理を終了する。
                        break
                    # 頂点 2k+1 を選択した場合
                    elif tmp == A[2*k+1]:
                        # A[k] と A[2k+1] を入れ替え k の値を 2k+1 に更新する。
                        A[k], A[2*k+1] = A[2*k+1], A[k]
                        k = 2*k + 1

        # x の値を 1 だけ減らす。
        x -= 1

    print(*A)

if __name__ == '__main__':
    main()