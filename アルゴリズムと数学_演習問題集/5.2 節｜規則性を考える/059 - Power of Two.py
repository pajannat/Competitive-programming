def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    if N % 4 == 1:
        print(2)
    elif N % 4 == 2:
        print(4)
    elif N % 4 == 3:
        print(8)
    elif N % 4 == 0:
        print(6)

if __name__ == '__main__':
    main()