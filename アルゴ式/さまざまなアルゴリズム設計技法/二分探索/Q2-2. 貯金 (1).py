def main():
    from sys import stdin
    input = stdin.readline

    # めぐる式二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midがansよりok側寄りの場合はTrueを返すように設計
        bank = N + 1
        for _ in range(5):
            bank = bank * arg + 1

        return bank > M

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        # 小数点以下まで扱う場合は(abs(ok - ng) > 0.01 などとする。
        while (abs(ok - ng) > 0.001): 
            # 小数点以下まで扱う場合は(ok + ng) / 2 とする。
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    # 入力を受け取る
    N, M = map(int, input().split())
    ng = 0
    ok = 11

    print(meguru_bisect(ng, ok))

if __name__ == '__main__':
    main()