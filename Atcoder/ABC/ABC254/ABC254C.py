def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A_list = [[] for _ in range(K)]

    # 処理
    for i in range(0, N, K):
        for j in range(K):
            if i+j > N-1:
                break
            # print(i+j)
            A_list[j].append(A[i+j])
        # print()
    
    # ソート
    for a in A_list:
        a.sort()
    
    # 併合
    ans = []
    for i in range(N):
        for j in range(K):
            if i > len(A_list[j])-1:
                break
            ans.append(A_list[j][i])

    flg = True
    for i, x in enumerate(ans):
        if i == 0:
            bef_x = x
        else:
            if bef_x > x:
                flg = False
                break
            else:
                bef_x = x
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()