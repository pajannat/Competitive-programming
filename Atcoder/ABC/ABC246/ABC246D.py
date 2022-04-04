def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    def f(a, b):
        return a*a*a + a*a*b + a*b*b + b*b*b

    # めぐる式二分探索
    def is_ok(N, a, b):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midがansよりok側寄りの場合はTrueを返すように設計
        X = f(a, b)
        return N <= X

    def meguru_bisect(N, a, ng, ok):
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
            if is_ok(N, a, mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = 10**18 + 1
    for a in range(10**6 + 1):
        b = meguru_bisect(N, a, -1, 10**6 + 1)
        ans = min(ans, f(a,b))

    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()