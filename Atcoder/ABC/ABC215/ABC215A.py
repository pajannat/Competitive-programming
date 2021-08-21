def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()

    if S == "Hello,World!":
        print("AC")
    else:
        print("WA")

if __name__ == '__main__':
    main()