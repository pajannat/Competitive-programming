def main():
    from sys import stdin
    input = stdin.readline


    # A 以上 B 以下の整数が素数かどうかを返す
    def EratosthenesAB(A, B):
        import math
        N = int(math.sqrt(B) + 1)
        # テーブル
        isprime = [True] * (N+1)
        isprime2 = [True] * (B - A + 1)

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

            # A 以上の最小の p の倍数
            start = A + (-A) % p
            if start == p:
                start = p * 2

            # A 以上 B 以下の整数のうち、p の倍数をふるう
            q = start
            while q <= B:
                isprime2[q - A] = False
                q += p

        # 1 以上 N 以下の整数が素数かどうか
        return isprime2
    
    # 入力を受け取る
    A, B = map(int, input().split())

    # A 以上 B 以下の整数 v が素数かどうか
    isprime2 = EratosthenesAB(A, B)

    # A 以上 B 以下の素数の数を出力
    print(sum(isprime2))

if __name__ == '__main__':
    main()