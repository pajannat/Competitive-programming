def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max_diff = -1

    # 処理
    for i in range(N):
        max_diff = max(A[i+1] - A[i], max_diff)
    
    # 答えを出力
    print(K - max_diff)


if __name__ == '__main__':
    main()