def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = input().rstrip()

    # 処理
    x = len(N) - 2
    
    # 答えを出力
    print(N[x:])


if __name__ == '__main__':
    main()