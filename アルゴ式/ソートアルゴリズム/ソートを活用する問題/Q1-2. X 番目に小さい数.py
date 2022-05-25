def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = list(map(int, input().split()))

    A.sort()

    # 出力
    for x in X:
        print(A[x])


if __name__ == '__main__':
    main()