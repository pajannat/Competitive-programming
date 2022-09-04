def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    n = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    # 処理
    for a in A:
        N = a
        p = 2
        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p
        cnt += e
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()