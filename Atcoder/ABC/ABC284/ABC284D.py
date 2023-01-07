def f(N):

    # N**(1/3) まで試し割っていく
    for A in range(2, N):
        # A * A * A <= N の範囲でよい
        if A * A * A > N:
            break

        # N が A で割り切れないならばスキップ
        if N % A != 0:
            continue
        # N が A で割り切れる場合
        else:
            if N % (A**2) == 0:
                p = A
                q = N // (A**2)
                return p, q
            else:
                p = int( (N // A)**(0.5) )
                q = A
                return p, q


def main():
    from sys import stdin
    input = stdin.readline


    # 入力
    T = int(input())
    N = [int(input()) for _ in range(T)]

    for i in range(T):

        # 素因数分解
        p, q = f(N[i])

        # 出力
        print(p, q)


if __name__ == '__main__':
    main()