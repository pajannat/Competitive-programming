def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    a, b, c = map(int, input().split())

    if a < c**b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()