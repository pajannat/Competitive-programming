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

def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    Q = int(input())
    isprime = Eratosthenes(300000)

    # 処理
    for _ in range(Q):
        X = int(input())
        if isprime[X] == True:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()