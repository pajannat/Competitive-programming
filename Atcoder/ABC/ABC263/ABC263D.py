def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, L, R = map(int, input().split())
    A = [0] + list(map(int, input().split())) + [0]
    LL = [0]*(N+2)
    RR = [0]*(N+2)
    ans = []

    # 処理
    LL[0] = 0
    for i in range(N):
        LL[i+1] = min(LL[i]+A[i+1], L*(i+1))

    RR[N+1] = 0
    for i in range(N+1)[::-1]:
        RR[i] = min(RR[i+1]+A[i], R*(N-i+1))

    for i in range(N+1):
        ans.append(LL[i]+RR[i+1])

    # 答えを出力
    print(min(ans))


if __name__ == '__main__':
    main()