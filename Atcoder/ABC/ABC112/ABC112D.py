def main():
    from sys import stdin
    input = stdin.readline

    # N の約数をすべて求める関数
    def calc_divisors(N):
        # 答えを表す集合
        res = []

        # 各整数 i が N の約数かどうかを調べる
        for i in range(1, N + 1):
            # √N で打ち切り
            if i * i > N:
                break
            
            # i が N の約数でない場合はスキップ
            if N % i != 0:
                continue

            # i は約数である
            res.append(i)

            # N ÷ i も約数である (重複に注意)
            if N // i != i:
                res.append(N // i)

        # 約数を小さい順に並び替えて出力
        res.sort()
        return res


    # 入力を受け取る
    N, M = map(int, input().split())
    ans = 1

    # 処理
    # a1, a2, ..., aN の最大公約数 Dより
    # a1 + a2 + ... + aN = M も Dを約数にもつ
    # M の約数 mのうち、a1 + a2 + ... + aN = M とできるものを探す

    # Mの約数
    M_divisors = calc_divisors(M)

    # M の約数 m を1つずつ試す
    for m in M_divisors:
        # N*m <= M であれば、mの倍数をa1, a2, ..., aNに分配可能
        # N*m > M だと、mをN個分配した時点でMを超えてしまい分配不可
        if N*m <= M:
            ans = max(m, ans)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()