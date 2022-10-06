def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    N = int(input())

    # 処理
    
    # 答えを出力
    print(2**int(math.log2(N)))


if __name__ == '__main__':
    main()