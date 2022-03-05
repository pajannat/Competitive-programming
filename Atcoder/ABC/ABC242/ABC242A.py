def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B, C, X = map(int, input().split())

    if X <= A:
        print(1)
    elif A+1 <= X <= B:
        print(C/(B-A))
    else:
        print(0)


if __name__ == '__main__':
    main()
# ------以上に