def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    ans = 1
    for i in range(N):
        ans = (ans * A[i]) % 10

    # 出力
    print(ans)

if __name__ == '__main__':
    main()