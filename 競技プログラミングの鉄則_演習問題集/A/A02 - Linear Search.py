def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # 処理
    
    # 答えを出力
    if X in A:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()