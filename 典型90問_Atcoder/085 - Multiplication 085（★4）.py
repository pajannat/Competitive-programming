def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
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
    
    divisors = calc_divisors(N)
    
    cnt = 0
    for a in divisors:
        for b in divisors:
            if N % (a*b) == 0:
                c = N // (a*b)
                if a <= b <= c:
                    cnt += 1

    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()