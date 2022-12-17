def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    SS = [[0]*M for _ in range(N)]
    for i in range(N):
        S = input().rstrip()
        for j in range(M):
            if S[j] == "o":
                SS[i][j] = 1
    
    cnt = 0

    # 処理
    for i in range(N-1):
        tmp = [0 for _ in range(M)]
        for j in range(i+1, N):
            for k in range(M):
                tmp[k] = max(SS[i][k], SS[j][k])

            if sum(tmp) == M:
                cnt += 1
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()