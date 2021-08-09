def main():
    from sys import stdin
    input = stdin.readline

    import numpy as np

    from itertools import permutations
    K = int(input())
    N = 4

    # 入力(配置条件)を格納。
    # この配置条件を満たすように配置する必要あり。
    RC = []
    for k in range(K):
        r, c = map(int, input().split())
        RC.append((r, c))

    # 入力(配置条件)を満たしているか判別する関数
    def input_rc_check(board):
        for rc in RC:
            if board[rc[0]][rc[1]] == 1:
                pass
            else:
                return False
        return True

    # 斜め方向に2つ以上配置されていないか判別する関数
    def diag_check(board):
        for i in range(-N+1, N):
            if np.sum(np.diag(board, k=i)) > 1:
                return False
            if np.sum(np.diag(np.fliplr(board), k=i)) > 1:
                return False
        return True

    # (3, 4, 1, 2, 0, 7, 6, 5)は
    # [0, 3],[1, 4],[2, 1],[3, 2],[4, 0],[5, 7],[6, 6],[7, 5]に配置
    # 縦横が重ならないパターンを全列挙。
    for p in permutations(range(N)):
        board = np.array([[0 for _ in range(N)] for _ in range(N)])
        for i, num in enumerate(p):
            board[i][num] = 1
        if input_rc_check(board) and diag_check(board):
            for r in p:
                ans = ['.'] * N
                ans[r] = 'Q'
                print(''.join(ans))
            exit()


if __name__ == '__main__':
    main()