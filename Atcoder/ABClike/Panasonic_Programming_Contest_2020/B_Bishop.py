def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())

    # 処理
    # H or W が 1のときは移動不可
    if H == 1 or W == 1:
        print(1)
    elif H % 2 == 1 and W % 2 == 1:
        print(H*W//2 + 1)
    else:
        print(H*W//2)


if __name__ == '__main__':
    main()