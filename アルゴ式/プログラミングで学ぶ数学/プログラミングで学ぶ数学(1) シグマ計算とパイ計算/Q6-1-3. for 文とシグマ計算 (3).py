def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += (A[i] + B[j])

    print(ans)

if __name__ == '__main__':
    main()