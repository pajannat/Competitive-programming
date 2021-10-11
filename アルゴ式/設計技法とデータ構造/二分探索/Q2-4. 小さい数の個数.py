def main():
    from sys import stdin
    input = stdin.readline

    import bisect
    
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aを昇順ソートしておく。
    A.sort()

    # Aの昇順ソートを保ったままB[k]をAに挿入することを考える。
    # B[k]の挿入箇所より左側の値が A[x] <= B[k] を満たすx
    for i in range(M):
        print(bisect.bisect_right(A, B[i]))

if __name__ == '__main__':
    main()