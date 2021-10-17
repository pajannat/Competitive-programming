def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    if (N % 100 == 0) and N != 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()