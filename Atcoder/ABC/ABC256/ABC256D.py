def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    R_max = 2*10**5
    imos = [0 for _ in range(R_max + 5)]
    interval = [0 for _ in range(R_max + 5)]
    ans = []

    # 処理
    for _ in range(N):
        L, R = map(int, input().split())
        # Rは右半開区間. 閉区間へと修正.
        R -= 1
        # imos法
        imos[L] += 1
        imos[R+1] -= 1

    # imos法のメモを区間に直す
    tmp = 0
    for i in range(R_max + 1):
        tmp += imos[i]
        interval[i] = tmp

    # imos法で求めた区間から答えを求める.
    now_num = -1
    next_num = -1
    for i in range(R_max):
        now_num = interval[i]
        next_num = interval[i+1]

        # 区間の始まり
        if now_num == 0 and next_num >= 1:
            new_L = i+1

        # 区間の終わり
        elif now_num >= 1 and next_num == 0:
            # 閉区間の終わりは new_R = i
            # ansは右半開区間で表現する必要あり. new_R = i+1 とする.
            new_R = i+1
            ans.append([new_L, new_R])

    # 答えを出力
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()