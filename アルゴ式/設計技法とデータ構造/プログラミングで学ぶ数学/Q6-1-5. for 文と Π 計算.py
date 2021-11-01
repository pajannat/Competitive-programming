def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    ans = A[0]
    for i in range(1, N):
        ans *= A[i]
        ans %= 10

    # 出力
    print(ans)

if __name__ == '__main__':
    main()