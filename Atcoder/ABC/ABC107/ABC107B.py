def main():
    from sys import stdin
    input = stdin.readline

    import numpy as np

    # 入力を受け取る
    H, W = map(int, input().split())
    INPUT = np.array([list(input().rstrip()) for _ in range(H)])

    # 処理
    del_H_idx = []
    del_W_idx = []

    # "." が連続する行を取り除く
    for i in range(H):
        if np.count_nonzero(INPUT[i, :] == '.') == W:
            del_H_idx.append(i)
    OUTPUT1 = np.delete(INPUT, del_H_idx, 0)

    # "." が連続する列を取り除く
    for i in range(W):
        if np.count_nonzero(OUTPUT1[:, i] == '.') == OUTPUT1.shape[0]:
            del_W_idx.append(i)
    OUTPUT2 = np.delete(OUTPUT1, del_W_idx, 1)
    
    # 答えを出力
    for i in range(OUTPUT2.shape[0]):
        print("".join(OUTPUT2[i]))


if __name__ == '__main__':
    main()