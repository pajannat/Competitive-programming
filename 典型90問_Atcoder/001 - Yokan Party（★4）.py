def main():
    from sys import stdin
    input = stdin.readline


    N, L = map(int, input().split())
    K = int(input())
    A_list = list(map(int, input().split()))

    # すべての切れ端をx以上とできるか判断
    def is_ok(x):
        cnt = 0
        cut_len = 0
        for a in A_list:
            # 長さがxを超え、残りの長さがx以上なら切る
            if (a - cut_len >= x) and (L - a >= x):
                # 切り込みの数を増やす
                cnt += 1
                # 最後に切り込み入れた場所を更新
                cut_len = a

        if cnt >= K:
            return True
        else:
            return False

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    ok = -1
    ng = L + 1
    ans = meguru_bisect(ng, ok)

    print(ans)

if __name__ == '__main__':
    main()