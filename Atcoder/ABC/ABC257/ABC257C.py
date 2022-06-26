def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()
    W = list(map(int, input().split()))

    hito = [[W[i], int(S[i])] for i in range(N)]
    hito.sort()

    child_cnt = [0 for _ in range(N)]
    adult_cnt = [0 for _ in range(N)]

    child_w_dict = {}
    adult_w_dict = {}
    for i in range(N):
        adult_child_flg = hito[i][1]
        # 子供の場合
        if adult_child_flg == 0:
            if hito[i][0] not in child_w_dict:
                child_w_dict[hito[i][0]] = 1
            else:
                child_w_dict[hito[i][0]] += 1

        # 大人の場合
        elif adult_child_flg == 1:
            if hito[i][0] not in adult_w_dict:
                adult_w_dict[hito[i][0]] = 1
            else:
                adult_w_dict[hito[i][0]] += 1

    W_for_dictkey = list(set(W))
    for i in range(len(W_for_dictkey)):
        W_for_dictkey.append(W_for_dictkey[i]-0.5)
        W_for_dictkey.append(W_for_dictkey[i]+0.5)
    W_for_dictkey = list(set(W_for_dictkey))
    W_for_dictkey.sort()

    total_child = 0
    total_adult = 0
    # 処理
    for k in W_for_dictkey:
        if k in child_w_dict:
            total_child += child_w_dict[k]
        if k in adult_w_dict:
            total_adult += adult_w_dict[k]

    min_diff = N+1
    child_cnt = 0
    adult_cnt = 0
    for k in W_for_dictkey:
        if k in child_w_dict:
            child_cnt += child_w_dict[k]
        if k in adult_w_dict:
            adult_cnt += adult_w_dict[k]

        tmp_diff = (total_child-child_cnt) + (adult_cnt)
        min_diff = min(min_diff, tmp_diff)
    
    ans = N - min_diff

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()