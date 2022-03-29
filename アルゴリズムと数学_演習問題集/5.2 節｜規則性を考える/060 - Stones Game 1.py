def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    if N % 4 == 0:
        print("Second")
    else:
        print("First")

if __name__ == '__main__':
    main()