def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 処理
    
    # 答えを出力
    for i in range(N):
        A, B = map(int, input().split())
        print(A+B)


if __name__ == '__main__':
    main()