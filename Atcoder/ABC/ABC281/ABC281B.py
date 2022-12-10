def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()


    # 処理
    # 文字列の長さを判定
    if len(S) != 8:
        print("No")
        exit()


    S_l = S[0]  # 先頭の文字
    S_r = S[len(S)-1]  # 末尾の文字
    num = S[1:len(S)-1]  # 中央の文字列

    flg = True

    # 文字列 num が数字か判定: num.isdigit()
    if num.isdigit():
        # 100000 以上 999999 以下の整数か
        if 100000 <= int(num) <= 999999:
            pass
        else:
            flg = False
    else:
        flg = False

    # 先頭と末尾が文字か判断
    if S_l.isalpha() and S_r.isalpha():
        pass
    else:
        flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()