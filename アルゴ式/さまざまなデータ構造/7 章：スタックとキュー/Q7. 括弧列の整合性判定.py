def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # 左括弧のcnt
    left_cnt = 0

    # 処理
    flg = True
    for s in S:
        if s == "(":
            left_cnt += 1
        elif s == ")":
            left_cnt -= 1
            # 左括弧の前に右括弧が出てきたらFalse
            if left_cnt < 0:
                flg = False
    
    # 右括弧が足りない場合False
    if left_cnt != 0:
        flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()