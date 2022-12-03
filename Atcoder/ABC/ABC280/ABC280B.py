def main():
    from sys import stdin
    input = stdin.readline

    
    # 入力を受け取る
    N = int(input())
    S = list(map(int, input().split()))
    A = []

    # 処理
    A.append(S[0])
    for i in range(N-1):
        A.append(S[i+1] - S[i])
    
    # 答えを出力
    print(*A)


if __name__ == '__main__':
    main()