def main():
    from sys import stdin
    input = stdin.readline

    # 階乗(自分で関数定義する場合)
    def for_factorial(n, MOD):
        val = 1
        for i in range(2, n + 1):
            val = (val*i) % MOD 
        return val

    # 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
    # (a**bをmで割った余り)
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


    MOD = 1000000007
    # 入力を受け取る
    X, Y = map(int, input().split())

    # 階乗を事前に計算しておく。繰り返し階乗の計算する場合にも定数時間で計算可。
    # 今回最大でも200000の階乗まで
    LIMIT = 200000
    fact = [None]*( LIMIT+1 )
    fact[0] = 1
    for i in range(1, LIMIT+1):
        fact[i] = fact[i-1]*i % MOD

    ans = 1

    XplusY_fact = fact[X+Y]

    X_fact = fact[X]
    X_fact = modpow(X_fact, MOD-2, MOD)

    Y_fact = fact[Y]
    Y_fact = modpow(Y_fact, MOD-2, MOD)

    ans = ans*XplusY_fact*X_fact*Y_fact % MOD

    print(ans)


if __name__ == '__main__':
    main()