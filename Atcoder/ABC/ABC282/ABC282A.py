def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    K = int(input())
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 処理
    
    # 答えを出力
    print(ABC[:K])


if __name__ == '__main__':
    main()