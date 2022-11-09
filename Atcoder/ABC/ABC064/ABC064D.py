def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = map(int, input().split())
    S = input().rstrip()
    S_list = list(S)
    left_kakko = ""
    right_kakko = ""
    cnt = 0

    # 処理
    for k in S_list:
        if k == "(":
            if cnt < 0:
                left_kakko = "(" * (-cnt) + left_kakko
                cnt = 1
            else:
                cnt += 1
        elif k == ")":
            cnt -= 1
    
    if cnt < 0:
        left_kakko = "(" * (-cnt) + left_kakko
    elif cnt > 0:
        right_kakko = ")" * cnt
    
    # 答えを出力
    print(left_kakko + S + right_kakko)


if __name__ == '__main__':
    main()