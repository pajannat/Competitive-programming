def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    for i in range(1, 50001):
        if int(i*1.08) == N:
            print(i)
            exit()
    
    print(":(")


if __name__ == '__main__':
    main()