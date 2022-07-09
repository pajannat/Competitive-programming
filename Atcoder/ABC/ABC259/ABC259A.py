def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, M, X, T, D = map(int, input().split())

    # 処理
    if X <= M <= N:
        ans = T
    elif 0 <= M < X:
        ans = T - D*(X-M)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()