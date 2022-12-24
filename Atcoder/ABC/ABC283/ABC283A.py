def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B = map(int, input().split())

    # 処理
    
    # 答えを出力
    print(A**B)


if __name__ == '__main__':
    main()