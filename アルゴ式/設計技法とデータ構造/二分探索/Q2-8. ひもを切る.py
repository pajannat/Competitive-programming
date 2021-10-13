def main():
    from sys import stdin
    input = stdin.readline

    # めぐる式二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る。
        # midが収束値ansよりok側寄りの場合はTrueを返すように設計

        # 設計例
        # (1) argが収束したときを考える
        # argが収束したとき -> ひもの本数 honsu(arg) は K に近づく
        # (2) argがok側寄りの場合を考える
        # argがok側寄りのとき -> 
        # 用意できるひもの本数 honsu(arg)は(1)のときより少なくなる
        # つまり、honsu(arg) < Kとなる。
        # (3) (2)の条件を判定条件として、returnに設定する。
        return honsu(arg) < K

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        # 小数点以下まで扱う場合は(abs(ok - ng) > 0.01 などとする。
        while (abs(ok - ng) > 1e-7): # 精度が十分良くなるまで計算
            # 小数点以下まで扱う場合は(ok + ng) / 2 とする。
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    # 長さ=nagasaのひもが何本用意できるか返す関数
    def honsu(nagasa):
        cnt = 0
        for i in range(N):
            cnt += L[i] // nagasa
        return cnt
    
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    # 同じ長さのひもを K 本用意するとき、
    # 用意できるひもの長さの最大値を0～(10**5+1)で探索
    ng = 0
    ok = 10**5 + 1
    
    # 出力
    print(meguru_bisect(ng, ok))

if __name__ == '__main__':
    main()