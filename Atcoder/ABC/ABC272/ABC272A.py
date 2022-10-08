def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # 処理
    
    # 答えを出力
    print(sum(A))


if __name__ == '__main__':
    main()