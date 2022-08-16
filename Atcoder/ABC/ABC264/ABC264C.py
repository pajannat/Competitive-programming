def main():
    from sys import stdin
    input = stdin.readline

    # bit全探索の組をcombinationsで生成する
    from itertools import combinations

    # 入力を受け取る
    H_A, W_A = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H_A)]

    H_B, W_B = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H_B)]

    # 処理

    # A_trans と Bが一致するかをチェックする
    def check(H_A_remain, W_A_remain):
        tmp_flg = True
        # 1マスずつ順に一致するかをチェック
        for i in range(H_B):
            for j in range(W_B):
                # 一致しなければ False
                if A[H_A_remain[i]][W_A_remain[j]] != B[i][j]:
                    tmp_flg = False
        return tmp_flg

    # A_trans と Bが一致することがあるかを記録する flg
    flg = False

    # bit全探索
    # 行列 A のどの行を残すか
    # H_AのうちH_B行分残す
    for H_A_remain in combinations(range(H_A), H_B):
        # 行列 A のどの列を残すか
        # W_AのうちW_B列分残す
        for W_A_remain in combinations(range(W_A), W_B):
            flg = check(H_A_remain, W_A_remain)

            # 行列 A の残りと行列 B が一致すれば Yes で exit
            if flg:
                print("Yes")
                exit()
    
    # 行列 A の残りと行列 B が一致することがない場合
    print('No')


if __name__ == '__main__':
    main()