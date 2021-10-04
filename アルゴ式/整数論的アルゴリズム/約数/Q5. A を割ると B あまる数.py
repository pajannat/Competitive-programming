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
    A, B = map(int, input().split())

    divisors = calc_divisors(A-B)
    cnt = 0
    for x in divisors:
        if x > B:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()