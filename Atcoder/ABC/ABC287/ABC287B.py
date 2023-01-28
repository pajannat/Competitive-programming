def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    S_list = []
    T_list = []
    cnt = 0

    for i in range(N):
        S = input().rstrip()
        S_list.append(S[3:])

    for i in range(M):
        T = input().rstrip()
        T_list.append(T)

    # 処理
    for S in S_list:
        for T in T_list:
            if S == T:
                cnt += 1
                break
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()