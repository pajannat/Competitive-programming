def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B, C, D = map(int, input().split())

    if A < C:
        print("Takahashi")
    elif A > C:
        print("Aoki")
    else:
        if B <= D:
            print("Takahashi")
        else:
            print("Aoki")

if __name__ == '__main__':
    main()