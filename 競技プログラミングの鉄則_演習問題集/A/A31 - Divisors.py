def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    ans = (N // 3) + (N // 5) - (N // 15)

    # 処理
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()