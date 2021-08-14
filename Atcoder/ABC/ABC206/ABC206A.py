def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    M = int(N * 1.08)

    if M < 206:
        print("Yay!")
    elif M == 206:
        print("so-so")
    elif M > 206:
        print(":(")


if __name__ == '__main__':
    main()