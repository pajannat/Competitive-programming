def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L_list = []
    R_list = []
    V_list = []
    for i in range(Q):
        L, R, V = map(int, input().split())
        L -= 1
        R -= 1
        L_list.append(L)
        R_list.append(R)
        V_list.append(V)
    
    # 処理
    ans = 0
    diff_list = []

    # 地殻変動前の不便さを計算
    # diff_list[i]はA[i]からA[i+1]に遷移する際の不便さの値
    for i in range(N):
        if i != N-1:
            diff_list.append(A[i+1]-A[i])
            ans += abs(A[i+1]-A[i])
        else:
            diff_list.append(A[i])
        
    # 答えを出力
    for i in range(Q):
        bef_diff_L = diff_list[L_list[i]-1]
        bef_diff_R = diff_list[R_list[i]]

        # 地殻変動の左端の処理
        if L_list[i] > 0:
            diff_list[L_list[i]-1] += V_list[i]
        # 地殻変動の右側の処理
        if R_list[i] < N-1:
            diff_list[R_list[i]] -= V_list[i]
        
        aft_diff_L = diff_list[L_list[i]-1]
        aft_diff_R = diff_list[R_list[i]]

        # 答えの計算
        ans = ans + (abs(aft_diff_L) - abs(bef_diff_L)) + (abs(aft_diff_R) - abs(bef_diff_R))

        # 答えを出力
        print(ans)

if __name__ == '__main__':
    main()