def main():
    from sys import stdin
    input = stdin.readline

    # 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
    # (a**bをmで割った余り)
    def modpow(a, b, m):
        p = a
        ans = 1
        # bの大きさにより計算範囲を変える。0<=i<=30でb=1073741823まで対応可
        for i in range(60): 
            # b のどこにbitが立っているか、1をひとつずつずらしながらAND演算
            # bはbitが立っている2**iの総和
            # -> 求める累乗数は p**(2**i)をすべて乗算したもの
            # bitが立っているときの p=a**(2**i) をansに乗算していく
            if ( b & (1 << i) ) != 0:
                ans = (ans*p) % m
            # p は a**1, a**2, a**4, a**8, ..., a**(2**i), ... と効率的に計算
            p = (p**2) % m
        return ans

    MOD = 1000000007
    # 入力を受け取る
    N = int(input())

    # 等比数列の和の公式
    a = 1
    r = 4
    n = N
    # a*(r**0) + a*r**1 + ... a*(r**n) までの和
    # S_r = a*(r**(n+1)-1) // (r-1)
    S_r = a*(modpow(r, n+1, MOD)-1)*modpow(r-1, MOD-2, MOD) % MOD

    print(S_r)

if __name__ == '__main__':
    main()