def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[]*M for _ in range(N)]
    for idx in range(N):
        A[idx] = [int(i) for i in input().split()]
    cnt = 0

    # 処理
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j]*B[j]
        sum += C

        if sum > 0:
            cnt += 1

    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()