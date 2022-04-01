def main():
    from sys import stdin
    input = stdin.readline

    MOD = 10**9 + 7
    # 入力を受け取る
    N, K = map(int, input().split())

    # 処理
    ans = K%MOD
    if N == 1:
        pass
    elif N == 2:
        ans = ans*(K-1)%MOD
    else:
        ans = ans*(K-1)%MOD
        ans = ans*pow(K-2, N-2, MOD)%MOD

    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()