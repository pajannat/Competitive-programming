def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())

    # 処理
    
    # 答えを出力
    if K % 2 == 0 and K >= 2*(N-1):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()