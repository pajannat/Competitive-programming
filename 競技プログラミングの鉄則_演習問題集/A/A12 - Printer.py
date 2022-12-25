def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    L_idx = 0
    R_idx = 10**9

    # 処理
    # めぐる式二分探索
    def is_ok(num, N, A, K):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midがansよりok側寄りの場合はTrueを返すように設計

        cnt = 0
        for i in range(N):
            cnt += (num // A[i])
        if cnt >= K:
            return True
        return False

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        # 小数点以下まで扱う場合は(abs(ok - ng) > 0.01 などとする。
        while (abs(ok - ng) > 1): # 精度が十分良くなるまで計算
            # 小数点以下まで扱う場合は(ok + ng) / 2 とする。
            mid = (ok + ng) // 2
            if is_ok(mid, N, A, K):
                ok = mid
            else:
                ng = mid
        return ok

    
    # 答えを出力
    print(meguru_bisect(L_idx, R_idx))


if __name__ == '__main__':
    main()