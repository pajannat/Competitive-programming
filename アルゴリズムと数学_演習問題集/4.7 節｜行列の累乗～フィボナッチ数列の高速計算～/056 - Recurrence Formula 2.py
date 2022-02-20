def main():
    from sys import stdin
    input = stdin.readline

    import numpy as np

    # 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
    # (a**bをmで割った余り)
    def modpow(a, b, m):
        p = a
        ans = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 2]], dtype=object)
        # bの大きさにより計算範囲を変える。0<=i<=30でb=1073741823まで対応可
        for i in range(60):
            # b のどこにbitが立っているか、1をひとつずつずらしながらAND演算
            # bはbitが立っている2**iの総和
            # -> 求める累乗数は p**(2**i)をすべて乗算したもの
            # bitが立っているときの p=a**(2**i) をansに乗算していく
            if ( b & (1 << i) ) != 0:
                ans = (np.dot(p, ans)) % m
            # p は a**1, a**2, a**4, a**8, ..., a**(2**i), ... と効率的に計算
            p = (np.dot(p, p)) % m
        return ans

    MOD = 10**9 + 7
    # 入力を受け取る
    N = int(input())

    A = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=object)

    print(sum(modpow(A, N-3, MOD)[2])%MOD)

if __name__ == '__main__':
    main()