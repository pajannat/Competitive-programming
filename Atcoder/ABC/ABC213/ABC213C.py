def main():
    from sys import stdin
    input = stdin.readline

    H, W, N = map(int, input().split())

    A_list = [0]*N
    B_list = [0]*N

    # 番号を付けてA,Bをリストに格納 (Ai, i), (Bi, i)
    for i in range(N):
        a, b = map(int, input().split())
        A_list[i] = (a, i)
        B_list[i] = (b, i)
    
    sort_A = sorted(A_list)
    sort_B = sorted(B_list)

    # sort_A[i][0]とsort_A[i-1][0]の間に存在する空白の数を計算
    diff_A = [0]*N
    for i in range(N):
        if i == 0:
            diff_A[i] = (sort_A[i][0] - 1, sort_A[i][1])
        elif sort_A[i][0] == sort_A[i-1][0]:
            diff_A[i] = (0, sort_A[i][1])
        else:
            diff_A[i] = (sort_A[i][0] - sort_A[i-1][0] - 1, sort_A[i][1])

    diff_A_cumsum = [0]*N
    sum_A = 0
    for i in range(N):
        sum_A += diff_A[i][0]
        diff_A_cumsum[i] = (diff_A[i][1], sum_A)

    # diff_A[i][1]順にソート(A_listの要素に対応する順)
    diff_A_cumsum = sorted(diff_A_cumsum)


    # sort_B[i][0]とsort_B[i-1][0]の間に存在する空白の数を計算
    diff_B = [0]*N
    for i in range(N):
        if i == 0:
            diff_B[i] = (sort_B[i][0] - 1, sort_B[i][1])
        elif sort_B[i][0] == sort_B[i-1][0]:
            diff_B[i] = (0, sort_B[i][1])
        else:
            diff_B[i] = (sort_B[i][0] - sort_B[i-1][0] - 1, sort_B[i][1])

    # sort_B[i][0]までに存在する空白の累積数を計算
    diff_B_cumsum = [0]*N
    sum_B = 0
    for i in range(N):
        sum_B += diff_B[i][0]
        diff_B_cumsum[i] = (diff_B[i][1], sum_B)
    
    # diff_B[i][1]順にソート(B_listの要素に対応する順)
    diff_B_cumsum = sorted(diff_B_cumsum)

    # (Ci, Di)を出力(空白行列を除去した後の(Ai, Bi))
    for i in range(N):
        C = A_list[i][0] - diff_A_cumsum[i][1]
        D = B_list[i][0] - diff_B_cumsum[i][1]
        print(C, D)

if __name__ == '__main__':
    main()