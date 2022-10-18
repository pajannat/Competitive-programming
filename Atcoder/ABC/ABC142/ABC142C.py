def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    ans = []

    # 処理
    # i -> 出席番号 -1
    # a -> 登校順
    for i, a in enumerate(A):
        B.append((a, i+1))
    B.sort()

    for b in B:
        ans.append(b[1])

    # 答えを出力
    print(*ans)


if __name__ == '__main__':
    main()