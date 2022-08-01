def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    Y = int(input())

    ans = -1
    # 処理
    for y in range(Y, 3010):
        if y % 4 == 2:
            ans = y
            break
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()