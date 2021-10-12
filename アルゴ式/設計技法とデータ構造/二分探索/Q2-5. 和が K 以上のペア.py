def main():
    from sys import stdin
    input = stdin.readline

    # めぐる式二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midがansよりok側寄りの場合はTrueを返すように設計
        return A[i] + A[arg] >= K

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
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Aを昇順ソートしておく。
    A.sort()

    cnt = 0
    for i in range(N):
        idx = meguru_bisect(-1, N)
        cnt += (N - idx)
    
    print(cnt)

if __name__ == '__main__':
    main()