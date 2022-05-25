def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    n = int(input())
    k = int(input())

    # 処理
    # 最大分割数 x
    # n = 3
    if n == 3:
        x = 1
    else:
        x = n // 2
    
    # 答えを出力
    if x >= k:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()