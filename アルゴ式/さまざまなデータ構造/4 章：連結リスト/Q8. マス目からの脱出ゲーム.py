def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    S = list(input().rstrip())
    right = [-1 for _ in range(N)]
    left = [-1 for _ in range(N)]
    # right, left の初期化. (各iを左右につなげた双方向連結リストの作成)
    for i in range(N):
        if i != N-1:
            right[i] = i + 1
        if i != 0:
            left[i] = i - 1

    # 処理
    direct = ">"
    idx = K
    cnt = 0
    while True:
        # 到達したマス(idx)を訪問済みとする
        # 次回通過時にはidxをスキップするために, idxへの連結を外す.
        # left[idx] -> idx -> right[idx] を left[idx] -> right[idx] とする
        right[left[idx]] = right[idx]
        # left[idx] <- idx <- right[idx] を left[idx] <- right[idx] とする
        left[right[idx]] = left[idx]
        

        # 移動方向を更新
        if S[idx] == ">":
            direct = ">"
        elif S[idx] == "<":
            direct = "<"
        
        # 次に進むマス
        if direct == ">":
            next_idx = right[idx]
        elif direct == "<":
            next_idx = left[idx]
        
        # cntを更新
        cnt += abs(next_idx - idx)

        # 現在位置を更新
        idx = next_idx

        # 移動先が端であれば終了
        if (idx == 0) or (idx == N-1):
            break

    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()