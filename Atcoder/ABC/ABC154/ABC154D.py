def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P_exp = [(1 + p) / 2 for p in P]
    P_exp_ruiseki = [0] * (N + 1)
    ans = 0

    # 処理
    P_exp_ruiseki[1] = P_exp[0]
    for i in range(1, N+1):
        P_exp_ruiseki[i] = P_exp_ruiseki[i-1] + P_exp[i-1]
    
    for i in range(N+1-K):
        ans = max(ans, P_exp_ruiseki[i+K] - P_exp_ruiseki[i])

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()