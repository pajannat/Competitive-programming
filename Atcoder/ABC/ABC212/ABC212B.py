def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()
    N_list = list(map(int, str(S)))

    if N_list[0] == N_list[1] == N_list[2] == N_list[3]:
        print("Weak")
        exit()

    weak_flg = True
    for i in range(len(N_list)-1):
        num = N_list[i]
        if num == 9:
            if N_list[i+1] == 0:
                pass
            else:
                weak_flg = False
        else:
            if N_list[i+1] == (num + 1):
                pass
            else:
                weak_flg = False
    
    if weak_flg:
        print("Weak")
    else:
        print("Strong")


if __name__ == '__main__':
    main()