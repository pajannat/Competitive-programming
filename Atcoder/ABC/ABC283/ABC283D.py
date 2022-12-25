def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()
    # ボールを入れる箱
    X = set()
    # 各括弧ごとの区画を[]として格納
    Y = [[]]

    # 処理
    for i, s in enumerate(S):
        # Yの末尾に新しい括弧の区画を追加
        if s == "(":
            Y.append([])
        # 箱からボールを取り出す
        elif s == ")":
            # 最新のYの区画Y[-1]に含まれるボールを取り出す
            for y in Y[-1]:
                X.discard(y)
            # Y[-1]の区画を削除
            Y.pop()
        else:
            # 箱にすでにsが格納されている場合は"No"
            if s in X:
                print("No")
                exit()
            # 箱にボールを格納する
            X.add(s)
            # Y[-1]がその時点でもっとも内側の括弧に対応する区画
            Y[-1].append(s)
    
    # 最後まで到達できれば"Yes"
    print("Yes")


if __name__ == '__main__':
    main()