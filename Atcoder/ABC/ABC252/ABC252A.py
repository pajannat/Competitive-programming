def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    # 答えを出力
    print(abc[N-97])


if __name__ == '__main__':
    main()