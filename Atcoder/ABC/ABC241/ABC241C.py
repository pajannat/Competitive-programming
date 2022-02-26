def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = []
    migi = [[0]*(N+1) for i in range(N+1)]
    sita = [[0]*(N+1) for i in range(N+1)]
    
    for i in range(N):
        S.append(input().rstrip())
    
    # 右方向の累積和
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == "#":
                cnt += 1
            migi[i][j] = cnt

    # 下方向の累積和
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j][i] == "#":
                cnt += 1
            sita[j][i] = cnt
    
    # 斜め右下方向のカウント
    def nanameR_ruiseki(a, b, S):
        for i in range(6):
            cnt = 0
            for j in range(6 - i):
                if S[a+i+j][b+j] == "#":
                    cnt += 1
            return cnt

    # 斜め左下方向のカウント
    def nanameL_ruiseki(a, b, S):
        for i in range(6):
            cnt = 0
            for j in range(6 - i):
                if S[a+i+j][b-j] == "#":
                    cnt += 1
            return cnt

    ok_flg = False

    tmp_m = 0
    tmp_s = 0
    for k in range(6):
        tmp_m = max(tmp_m, migi[k][5]-migi[k][-1])
        tmp_s = max(tmp_s, sita[5][k]-sita[-1][k])
    tmp_ms = nanameR_ruiseki(0, 0, S)
    tmp_hs = nanameL_ruiseki(0, 5, S)
    if (tmp_m>=4) or (tmp_s>=4) or (tmp_ms>=4) or (tmp_hs>=4):
        ok_flg = True

    for i in range(N-5):
        for j in range(N-5):
            tmp_m = 0
            tmp_s = 0
            for k in range(6):
                tmp_m = max(tmp_m, migi[i+k][j+5]-migi[i+k][j-1])
                tmp_s = max(tmp_s, sita[i+5][j+k]-sita[i-1][j+k])
            tmp_ms = nanameR_ruiseki(i, j, S)
            tmp_hs = nanameL_ruiseki(i, j+5, S)
            if (tmp_m>=4) or (tmp_s>=4) or (tmp_ms>=4) or (tmp_hs>=4):
                ok_flg = True
    
    if ok_flg:
        print("Yes")
    else:
        print("No")
    

if __name__ == '__main__':
    main()