def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    # 出力
    print(sum(A[:K]))

if __name__ == '__main__':
    main()