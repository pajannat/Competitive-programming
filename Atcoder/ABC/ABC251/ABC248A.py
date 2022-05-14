def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()

    # 処理
    SSS = S*10
    
    # 答えを出力
    print(SSS[:6])


if __name__ == '__main__':
    main()