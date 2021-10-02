def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()
    T = input().rstrip()

    diff_list = []

    for i in range(len(S)):
        if S[i] == T[i]:
            pass
        else:
            diff_list.append((S[i], T[i], i))
    
    if len(diff_list) == 0:
        print("Yes")
    elif len(diff_list) == 2:
        if (diff_list[0][0] == diff_list[1][1]) and (diff_list[0][1] == diff_list[1][0]) and ((diff_list[1][2] - diff_list[0][2]) == 1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()