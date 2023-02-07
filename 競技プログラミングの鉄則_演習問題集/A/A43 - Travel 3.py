def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, L = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = input().split()
        A.append(int(a))
        B.append(b)
    
    ans = 0

    # 処理
    # 折り返しを考慮せず、すれ違うと考えてもよい
    for i in range(N):
        if B[i] == "E":
            ans = max(ans, L-A[i])
        else:
            ans = max(ans, A[i])

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()