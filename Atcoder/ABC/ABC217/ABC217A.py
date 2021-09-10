def main():
    from sys import stdin
    input = stdin.readline

    S, T = input().split()
    str_list = [S, T]
    str_list.sort()

    if str_list[0] == S:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()