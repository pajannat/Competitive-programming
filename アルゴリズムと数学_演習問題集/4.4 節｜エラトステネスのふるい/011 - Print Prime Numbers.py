def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    # 2 <= x <= n の整数の集合を用意
    primes = set(range(2, N+1))
    # xより大きなxの倍数を除去していく(2 <= x <= n**0.5)
    for i in range(2, int(N**0.5+1)):
        # 集合primesから、集合(range(i*2, n+1, i))を除去
        primes.difference_update(range(i*2, N+1, i))
    primes=list(primes)

    print(*primes)

if __name__ == '__main__':
    main()