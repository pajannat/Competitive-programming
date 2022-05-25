def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, X = map(int, input().split())
    ans = X

    # 出力
    print(ans)
    for i in range(N):
        ans += 500
        print(ans)

if __name__ == '__main__':
    main()