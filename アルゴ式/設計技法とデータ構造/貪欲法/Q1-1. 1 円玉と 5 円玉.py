def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    five = N // 5
    one = N % 5

    print(one+five)

if __name__ == '__main__':
    main()