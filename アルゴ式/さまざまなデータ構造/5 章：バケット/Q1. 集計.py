def main():
    from sys import stdin
    input = stdin.readline

    from collections import Counter
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 処理
    S = Counter(A)
    for _ in range(Q):
        x = int(input())
        print(S[x])


if __name__ == '__main__':
    main()