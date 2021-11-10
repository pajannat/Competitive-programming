def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_and_B = list(set(A) & set(B))
    A_and_B.sort()

    # 出力
    for ab in A_and_B:
        print(ab)

if __name__ == '__main__':
    main()