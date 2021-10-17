def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    
    ruiseki_len = [0]
    ruiseki_sec = [0]
    for i in range(1, len(AB)+1):
        ruiseki_len.append(ruiseki_len[i-1]+AB[i-1][0])
        ruiseki_sec.append(ruiseki_sec[i-1]+(AB[i-1][0]/AB[i-1][1]))

    # めぐる式二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midがansよりok側寄りの場合はTrueを返すように設計
        arg_idx = bisect.bisect_left(ruiseki_len, arg)
        left_time = ruiseki_sec[arg_idx-1] + (arg - ruiseki_len[arg_idx-1])/AB[arg_idx-1][1]
        right_time = ruiseki_sec[-1] - left_time

        # 設計例
        # (1) argが収束したときを考える
        # argが収束したとき -> left_time は right_time に近づく
        # (2) argがok側寄りの場合を考える
        # argがok側寄りのとき -> 
        # つまり、left_time >= right_timeとなる。
        # (3) (2)の条件を判定条件として、returnに設定する。
        return left_time >= right_time

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        # 小数点以下まで扱う場合は(abs(ok - ng) > 0.01 などとする。
        while (abs(ok - ng) > 0.0000001): # 精度が十分良くなるまで計算
            # 小数点以下まで扱う場合は(ok + ng) / 2 とする。
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    ng = 0
    ok = ruiseki_len[-1]+1

    print(meguru_bisect(ng, ok))

if __name__ == '__main__':
    main()