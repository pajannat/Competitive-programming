def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    X, Y, Z = map(int, input().split())

    # 処理
    # X, Y の符号を調べる
    # X, Y がどちらも正
    if X > 0 and Y > 0:
        # 原点とXの間に壁Yがある場合
        if X > Y:
            # ハンマーをZに取りに行く
            # ハンマーへ到達不可の場合
            if Z > Y:
                print(-1)
            # ハンマーに到達可能な場合
            else:
                if Z < 0:
                    print(abs(X) + 2*abs(Z))
                else:
                    print(abs(X))
        else:
            print(abs(X))
    # X, Y がどちらも負
    elif X < 0 and Y < 0:
        # 原点とXの間に壁Yがある場合
        if X < Y:
            # ハンマーをZに取りに行く
            # ハンマーへ到達不可の場合
            if Z < Y:
                print(-1)
            # ハンマーに到達可能な場合
            else:
                if Z > 0:
                    print(abs(X) + 2*abs(Z))
                else:
                    print(abs(X))
        else:
            print(abs(X))
    # X, Y が逆符号
    else:
        print(abs(X))


if __name__ == '__main__':
    main()