def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    print(S[-1])


if __name__ == '__main__':
    main()