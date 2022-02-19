def main():
    from sys import stdin
    input = stdin.readline

    A, B, C, D = map(int, input().split())

    # 素数リスト作成(エラトステネスの篩)
    n = B+D+1
    # 2 <= x <= n の整数の集合を用意
    primes = set(range(2, n))
    # xより大きなxの倍数を除去していく(2 <= x <= n**0.5)
    for i in range(2, int(n**0.5+1)):
        # 集合primesから、集合(range(i*2, n+1, i))を除去
        primes.difference_update(range(i*2, n+1, i))

    T_flg = False
    for i in range(A, B+1):
        # Aokiが勝てる選び方があるか？(素数となる数をAokiは選べるか?)
        # Aokiが作れる数の中に、素数はあるか?
        if len( list(set(range(C+i, D+i+1))&primes) ) == 0:
            T_flg = True
        if T_flg:
            break
    
    if T_flg:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == '__main__':
    main()