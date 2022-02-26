def main():
    from sys import stdin
    input = stdin.readline

    A, B = map(int, input().split())

    if B-A == 1:
        print("Yes")
    elif A == 1 and B == 10:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()