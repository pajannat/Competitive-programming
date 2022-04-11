def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    R_idx = 0
    L_idx = 0
    K_dic = {}
    max_len = 0

    # 処理
    # 尺取り法
    # 左側のidxと右側のidxをそれぞれL_idx, R_idxで管理
    for i in range(N):
        R_idx = i
        # K_dicでそれぞれの数の個数管理
        # K_dicに数A[i]がなければ追加
        if A[i] not in K_dic:
            K_dic[A[i]] = 1
        # K_dicに数A[i]があれば個数+1
        else:
            K_dic[A[i]] += 1

        # K_dicに含まれる数がK種類を超えている限り、L_idxを前に進める
        while len(K_dic) > K:
            # K_dicから数A[L_idx]をひとつ取り出す
            K_dic[A[L_idx]] -= 1
            # 上記操作により、K_dicの中の数A[L_idx]の個数が0になったら、K_dicから削除
            if K_dic[A[L_idx]] == 0:
                K_dic.pop(A[L_idx])
            # L_idxを更新
            L_idx += 1

        # max_lenを更新
        max_len = max(max_len, R_idx-L_idx+1)
    
    # 答えを出力
    print(max_len)

if __name__ == '__main__':
    main()