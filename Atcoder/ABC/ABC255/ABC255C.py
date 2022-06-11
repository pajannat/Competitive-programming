def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    X, A, D, N = map(int, input().split())

    ans = -1

    # 処理
    X = X - A
    A = 0
    AN = (N-1)*D
    min_A = min(A, AN)
    max_A = max(A, AN)

    if X <= min_A:
        ans = min_A - X
    elif max_A <= X:
        ans = X - max_A
    elif min_A < X < max_A:
        num = X // D
        min_adj = num*D
        max_adj = (num+1)*D
        ans = min(abs(X-min_adj), abs(max_adj-X))
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()