def main():
    from sys import stdin
    input = stdin.readline

    MOD = 1000000007

    # 入力を受け取る
    a, b = map(int, input().split())

    # 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
    def modpow(a, b, m):
        p = a
        ans = 1
        # bの大きさにより計算範囲を変える。0<=i<=30でb=1073741823まで対応可
        for i in range(30):
            # b のどこにbitが立っているか、1をひとつずつずらしながらAND演算
            # bはbitが立っている2**iの総和
            # -> 求める累乗数は p**(2**i)をすべて乗算したもの
            # bitが立っているときの p=a**(2**i) をansに乗算していく
            if ( b & (1 << i) ) != 0:
                ans = (ans*p) % m
            # p は a**1, a**2, a**4, a**8, ..., a**(2**i), ... と効率的に計算
            p = (p**2) % m
        return ans

    print(modpow(a, b, MOD))

if __name__ == '__main__':
    main()