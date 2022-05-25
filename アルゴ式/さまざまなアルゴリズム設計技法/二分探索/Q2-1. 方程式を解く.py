def main():
    from sys import stdin
    input = stdin.readline

    # めぐる式二分探索
    def is_ok(arg):
        return arg*(arg*(arg+1)+2)+3 > N

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1e-4):
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    ng = -1
    ok = 100000100001
    N = int(input())
    # 出力
    print(meguru_bisect(ng, ok))

if __name__ == '__main__':
    main()