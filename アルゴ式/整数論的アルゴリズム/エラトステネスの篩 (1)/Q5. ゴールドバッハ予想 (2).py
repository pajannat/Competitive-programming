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
    
    # 入力を受け取る
    N = int(input())

    # N 以下の素数をすべて求める
    isprime = Eratosthenes(N)

    # N以下の双子素数の組数をカウント
    cnt = 0
    for i in range(N-1):
        if i > N-i:
            continue

        if isprime[i] and isprime[N-i]:
            cnt += 1

    # N以下の素数の数を出力
    print(cnt)

if __name__ == '__main__':
    main()