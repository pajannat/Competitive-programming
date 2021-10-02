def main():
    from sys import stdin
    input = stdin.readline

    # 1 以上 N 以下の整数が素数かどうかを返す
    def Eratosthenes(N):
        # テーブル
        isprime = [True] * (N+1)

        # 0, 1 は予めふるい落としておく
        isprime[0], isprime[1] = False, False

        # ふるい
        for p in range(2, N+1):
            # すでに合成数であるものはスキップする
            if not isprime[p]:
                continue

            # p 以外の p の倍数から素数ラベルを剥奪
            q = p * 2
            while q <= N:
                isprime[q] = False
                q += p

        # 1 以上 N 以下の整数が素数かどうか
        return isprime

    # 1 以上 N 以下の整数が素数かどうかを返す
    def Eratosthenes235(N):
        # テーブル
        isprime = [True] * (N+1)

        # 0, 1 は予めふるい落としておく
        isprime[0], isprime[1] = False, False

        # ふるい
        hurui = [2, 3, 5]
        for p in hurui:
            # すでに合成数であるものはスキップする
            if not isprime[p]:
                continue

            # p 以外の p の倍数から素数ラベルを剥奪
            q = p * 2
            while q <= N:
                isprime[q] = False
                q += p

        # 1 以上 N 以下の整数が素数かどうか
        return isprime

    # 30 以下の素数をすべて求める
    isprime = Eratosthenes(100)

    # 2, 3, 5の倍数をふるいにかける 
    isprime235 = Eratosthenes235(100)

    cnt = 0
    for i in range(100):
        if isprime[i] != isprime235[i]:
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()