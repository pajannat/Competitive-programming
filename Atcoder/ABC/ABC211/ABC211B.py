def main():
    from sys import stdin
    input = stdin.readline

    S1 = input().rstrip()
    S2 = input().rstrip()
    S3 = input().rstrip()
    S4 = input().rstrip()
    S_list = [S1, S2, S3, S4]

    if ("H" in S_list) and ("2B" in S_list) and ("3B" in S_list) and ("HR" in S_list):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()