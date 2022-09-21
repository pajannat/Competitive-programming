def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()
    A = [0 for _ in range(len(S)+1)]

    # 処理
    for i in range(len(S)):
        if S[i] == '<':
            A[i+1] = max(A[i+1], A[i]+1)
        
    for i in reversed(range(len(S))):
        if S[i] == '>':
            A[i] = max(A[i], A[i+1]+1)

    # 答えを出力
    print(sum(A))


if __name__ == '__main__':
    main()