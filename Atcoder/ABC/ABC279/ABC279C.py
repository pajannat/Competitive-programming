def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, W = map(int, input().split())
    S = []
    T = []
    S_r = [[] for _ in range(W)]
    T_r = [[] for _ in range(W)]


    # 処理
    for _ in range(N):
        S.append(input().rstrip())
    for _ in range(N):
        T.append(input().rstrip())
    
    for i in range(N):
        for j in range(W):
            S_r[j].append(S[i][j])
            T_r[j].append(T[i][j])
    
    S_r.sort()
    T_r.sort()
    flg = True
    for i in range(W):
        if S_r[i] != T_r[i]:
            flg = False

    # 答えを出力
    if flg == True:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()