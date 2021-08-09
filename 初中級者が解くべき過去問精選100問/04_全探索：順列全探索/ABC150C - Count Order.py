def main():
    from sys import stdin
    input = stdin.readline

    from itertools import permutations

    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    perm_list = list(permutations(range(1, N+1)))

    index_P = perm_list.index(P)
    index_Q = perm_list.index(Q)

    print(abs(index_P - index_Q))

if __name__ == '__main__':
    main()