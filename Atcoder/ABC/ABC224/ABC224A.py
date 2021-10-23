def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    S = input().rstrip()

    if S[-2:] == "er":
        print("er")
    else:
        print("ist")

if __name__ == '__main__':
    main()