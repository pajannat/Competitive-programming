def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = [-1] + [int(s) for s in list(input().rstrip())]

    # 処理
    flg = False
    if S[1] == 0:
        # 4が倒れている場合
        if S[4] == 0:
            left_flg = False
            right_flg = False
            if S[7] == 1:
                left_flg = True
            for i in range(1, 11):
                if i == 4 or i == 7:
                    continue
                if S[i] == 1:
                    right_flg = True
            
            if left_flg and right_flg:
                print("Yes")
                exit()

        # 2,8が倒れている場合
        if S[2] == 0 and S[8] == 0:
            left_flg = False
            right_flg = False
            if S[4] == 1 or S[7] == 1:
                left_flg = True
            for i in range(1, 11):
                if i == 2 or i == 8 or i == 4 or i == 7:
                    continue
                if S[i] == 1:
                    right_flg = True
            
            if left_flg and right_flg:
                print("Yes")
                exit()

        # 1,5が倒れている場合
        if S[1] == 0 and S[5] == 0:
            left_flg = False
            right_flg = False
            if S[2] == 1 or S[4] == 1 or S[7] == 1 or S[8] == 1:
                left_flg = True

            if S[3] == 1 or S[6] == 1 or S[9] == 1 or S[10] == 1:
                right_flg = True
            
            if left_flg and right_flg:
                print("Yes")
                exit()

        # 3,9が倒れている場合
        if S[3] == 0 and S[9] == 0:
            left_flg = False
            right_flg = False
            if S[2] == 1 or S[4] == 1 or S[5] == 1 or S[7] == 1 or S[8] == 1:
                left_flg = True

            if S[6] == 1 or S[10] == 1:
                right_flg = True
            
            if left_flg and right_flg:
                print("Yes")
                exit()

        # 6が倒れている場合
        if S[6] == 0:
            left_flg = False
            right_flg = False
            if S[2] == 1 or S[3] == 1 or S[4] == 1 or S[5] == 1 or S[7] == 1 or S[8] == 1 or S[9] == 1:
                left_flg = True

            if S[10] == 1:
                right_flg = True
            
            if left_flg and right_flg:
                print("Yes")
                exit()

    
    # 答えを出力
    print("No")


if __name__ == '__main__':
    main()