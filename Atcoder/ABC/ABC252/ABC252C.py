def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = []
    for i in range(N):
        S.append(input().rstrip())
    
    S_cnt = [[0]*10 for _ in range(10)]
    for s in S:
        for i, num in enumerate(s):
            S_cnt[int(num)][i] += 1

    # 処理
    cnt = 10000000
    # 0~9のうちどれに注目?
    for i in range(10):
        tmp_cnt = 0
        # 何番目の出現に注目？
        for j in range(10):
            c_ij = S_cnt[i][j]
            tmp_cnt = max(tmp_cnt, 10*(c_ij-1)+j)
        cnt = min(cnt, tmp_cnt)

    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()