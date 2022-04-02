def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    N = int(input())

    # 処理

    # 割ることができた回数が素因数の数
    # 範囲はp * p <= N の範囲でよい
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

    # Nを素因数分解する
    pf = prime_factorize(N)

    # 出力    
    cnt = 0

    for p, e in pf:
        cnt += e
    
    ans = math.ceil(math.log2(cnt))

    print(ans)


if __name__ == '__main__':
    main()