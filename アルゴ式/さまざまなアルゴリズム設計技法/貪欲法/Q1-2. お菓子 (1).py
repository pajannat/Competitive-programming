def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    cnt = 0
    okashi = N
    while okashi != 0:
        if okashi % 2 == 0:
            cnt += 1
            okashi = okashi // 2
        else:
            cnt += 1
            okashi -= 1

    print(cnt)

if __name__ == '__main__':
    main()