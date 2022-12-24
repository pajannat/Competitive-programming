def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())
    used = set()

    # 処理
    for i, s in enumerate(S):
        if s == '(':
            pass
        elif s == ')':
            used = set()
        else:
            if s in used:
                print("No")
                exit()
            used.add(s)

    # 答えを出力
    print("Yes")


if __name__ == '__main__':
    main()