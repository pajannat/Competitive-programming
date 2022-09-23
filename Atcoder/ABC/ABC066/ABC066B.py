def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())

    # 処理
    # S の末尾1文字を削除した文字列 SS
    SS = S[0:-1]
    # SS の文字数が奇数のときは末尾1文字を削除
    if len(SS) % 2 != 0:
        SS.pop()
    
    while True:
        left_SS = ''.join(SS[:len(SS)//2])
        right_SS = ''.join(SS[len(SS)//2:])

        if left_SS == right_SS:
            break
        else:
            SS.pop()
            SS.pop()
    
    ans = len(SS)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()