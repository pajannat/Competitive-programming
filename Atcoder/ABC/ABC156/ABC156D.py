def main():
    from sys import stdin
    input = stdin.readline


    # 高速なcmb演算 2
    # 答えは必ず整数になるので，
    # 先に約分を行って分母を消してから残りを掛け合わせる
    # cmb演算結果を素数 mで割った余りを求める場合
    # 計算途中で都度mod m を計算することで数が大きくなりすぎないようにする
    # (数が大きくなると計算に時間がかかるようになる)
    def cmb(n, r, m):
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2,r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1,r,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])
                result %= m

        return result


    # 入力を受け取る
    n, a, b = map(int, input().split())
    ans = 0
    m = 10**9 + 7

    # 処理
    # 花束を1本以上選ぶ方法は 2**n - 1
    # pow(2, n, m) は繰り返し二乗法で計算されるため高速
    ans = pow(2, n, m) - 1

    # (2**n - 1) - nCa - nCb
    ans = (ans - cmb(n, a, m) - cmb(n, b, m)) % m
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()