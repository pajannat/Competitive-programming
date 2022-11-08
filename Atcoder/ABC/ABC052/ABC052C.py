# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    # 答えを表す可変長配列
    res = []

    # √N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p

        # 答えに追加
        res.append((p, e))

    # 素数が最後に残ることがありうる
    if N != 1:
        res.append((N, 1))

    return res

def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    MOD = 10**9 + 7
    N = int(input())
    prime_fact = prime_factorize(math.factorial(N))
    ans = 1

    # 処理
    for p, n in prime_fact:
        ans = ans*(n + 1) % MOD

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()