def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S_list = []
    for _ in range(N):
        S_list.append(input().rstrip())

    # 処理
    flg = True

    # すべての文字列に対して、1文字目は H, D, C, S のどれかである。
    for S in S_list:
        if S[0] not in ["H", "D", "C", "S"]:
            flg = False

    # すべての文字列に対して、2文字目は A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K のどれかである。
    for S in S_list:
        if S[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            flg = False

    # すべての文字列は相異なる。
    for idx, S in enumerate(S_list):
        if S in S_list[:idx] or S in S_list[idx+1:]:
            flg = False


    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()