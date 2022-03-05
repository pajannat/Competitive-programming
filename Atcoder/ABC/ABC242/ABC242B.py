def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())
    S.sort()
    print(''.join(S))


if __name__ == '__main__':
    main()