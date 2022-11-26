def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    P = [0] + list(map(int, input().split()))
    used = [0]*(N+1)
    indices = [-1]*(N+1)
    ans = []

    # 処理
    # P内の各数字がどこにあるかを事前に調べる
    for i in range(N+1):
        indices[P[i]] = i

    # swap操作を実行
    # 1から順に先頭に移動させる
    start_idx = 1
    end_idx = indices[1]
    while True:
        for j in range(end_idx-1, start_idx-1, -1):
            P[j], P[j + 1] = P[j + 1], P[j]
            ans.append(j)
            used[j] = 1
        # end_idx - 1 まで整列(swap操作)が完了
        # 次は idx:end_idx に num:end_idx を移動させる
        start_idx = end_idx
        end_idx = indices[end_idx]
        if start_idx >= end_idx or start_idx >= len(P) - 1:
            break
    
    # 答えを出力
    # すべてのswap操作を実行していない場合
    if sum(used) != N-1:
        print(-1)
        exit()
    else:
        for i in range(1, N+1):
            # 昇順に並んでいない場合
            if P[i] != i:
                print(-1)
                exit()

        # swap順を出力
        for a in ans:
            print(a)


if __name__ == '__main__':
    main()