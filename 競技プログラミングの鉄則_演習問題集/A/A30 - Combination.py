# mod 計算の ÷ b は × (b ** (mod-2))で計算する
def mod_a_div_b(a, b, m):
    return (a * pow(b, m-2, m)) % m

def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    n, r = map(int, input().split())
    MOD = 1000000007
    ans = 0

    # 処理
    LIMIT = 100000
    fact = [None]*( LIMIT+1 )
    fact[0] = 1
    for i in range(1, LIMIT+1):
        fact[i] = fact[i-1]*i % MOD
    
    # mod 計算の ÷ b は × (b ** (mod-2))で計算する
    a = fact[n]
    b = (fact[r] * fact[n-r]) % MOD
    ans = mod_a_div_b(a, b, MOD)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()