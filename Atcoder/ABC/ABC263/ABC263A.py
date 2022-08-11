def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    ABCDE = list(map(int, input().split()))
    cnt_list = [0] * 14

    # 処理
    for num in ABCDE:
        cnt_list[num] += 1
    
    cnt2_flg = False
    cnt3_flg = False

    for cnt in cnt_list:
        if cnt == 2:
            cnt2_flg = True
        if cnt == 3:
            cnt3_flg = True
    
    # 答えを出力
    if cnt2_flg and cnt3_flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()