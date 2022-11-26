def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    S = input().rstrip()
    T = input().rstrip()

    # 処理
    if T in S:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()