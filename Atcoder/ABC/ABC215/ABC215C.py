def main():
    from sys import stdin
    input = stdin.readline

    from itertools import permutations

    S, K = input().split()
    K = int(K)

    S_list = list(permutations(S, len(S)))
    S_list = set(S_list)
    S_list = list(S_list)
    S_list.sort()

    print(''.join(S_list[K-1]))


if __name__ == '__main__':
    main()