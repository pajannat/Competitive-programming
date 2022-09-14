def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, A, B = map(int, input().split())
    S = input().rstrip()

    # 予選の通過が確定した参加者の現在の数
    tuuka = 0

    # 予選の通過が確定した海外の学生の数
    tuuka_kaigai = 0

    # 処理
    for s in S:
        # 国内の学生の場合
        if s == "a":
            # tuuka < A + B であれば通過
            if tuuka < A + B:
                print("Yes")
                tuuka += 1
            else:
                print("No")

        # 海外の学生の場合
        elif s == "b":
            # tuuka < A + B かつ tuuka_kaigai < B であれば通過
            if tuuka < A + B and tuuka_kaigai < B:
                print("Yes")
                tuuka += 1
                tuuka_kaigai += 1
            else:
                print("No")

        # それ以外の場合
        # 予選通過しない
        else:
            print("No")


if __name__ == '__main__':
    main()