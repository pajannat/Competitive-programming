def main():
    from sys import stdin
    input = stdin.readline

    N,K = map(int,input().split())

    def g1(num):
        num_str = list(str(num))
        num_str = sorted(num_str, reverse=True)
        num_g1 = ''.join(num_str)
        return int(num_g1)

    def g2(num):
        num_str = list(str(num))
        num_str = sorted(num_str, reverse=False)
        num_g2 = ''.join(num_str)
        return int(num_g2)

    def f(x):
        return g1(x)-g2(x)

    ai = N
    for idx in range(K):
        ai = f(ai)

    print(ai)

if __name__ == '__main__':
    main()