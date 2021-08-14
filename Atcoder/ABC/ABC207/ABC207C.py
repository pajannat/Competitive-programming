def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    segments_list = []

    # 入力をsegments_listに格納
    for i in range(N):
        ti,li,ri = map(int,input().split())
        if ti == 1:
            segments_list.append([li,ri])
        elif ti == 2:
            # 区間[X,Y) => [X,Y]に置換
            segments_list.append([li,ri - 0.1])
        elif ti == 3:
            # 区間(X,Y] => [X,Y]に置換
            segments_list.append([li + 0.1,ri])
        else:
            # 区間(X,Y) => [X,Y]に置換
            segments_list.append([li + 0.1,ri - 0.1])

    # すべての区間が共通部分をもつ場合の数
    common_part_num_max = N*(N-1)//2

    # 共通部分を持たないパターンを全探索してカウント
    not_common_part_num = 0
    for i in range(N):
        li = segments_list[i][0]
        ri = segments_list[i][1]
        for j in range(N):
            lj = segments_list[j][0]
            rj = segments_list[j][1]
            if i == j:
                continue
            elif ri < lj:
                not_common_part_num += 1
            elif rj < li:
                not_common_part_num += 1
    not_common_part_num = not_common_part_num//2

    ans = common_part_num_max - not_common_part_num

    print(ans)

if __name__ == '__main__':
    main()