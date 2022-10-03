def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    a, b = map(int, input().split())
    ab = int(str(a) + str(b))

    # 処理
    # abが平方数であるか判別
    for i in range(100101):
        if i*i > ab:
            break

        if ab == i*i:
            print("Yes")
            exit()
    
    print("No")


if __name__ == '__main__':
    main()