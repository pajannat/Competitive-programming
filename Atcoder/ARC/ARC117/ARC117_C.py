def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    c = input().rstrip()
    c_lst0 = [i for i in c]
    c_lst = [[""]*len(c) for i in range(len(c))]
    c_lst[0] = c_lst0


    for idx in range(1,len(c)):
        for idx2 in range(len(c)-idx):
            if c_lst[idx-1][idx2] == c_lst[idx-1][idx2+1]:
                c_lst[idx][idx2] = c_lst[idx-1][idx2]
            elif c_lst[idx-1][idx2] == "B" and c_lst[idx-1][idx2+1] == "W":
                c_lst[idx][idx2] = "R"
            elif c_lst[idx-1][idx2] == "W" and c_lst[idx-1][idx2+1] == "R":
                c_lst[idx][idx2] = "B"
            elif c_lst[idx-1][idx2] == "R" and c_lst[idx-1][idx2+1] == "B":
                c_lst[idx][idx2] = "W"
            elif c_lst[idx-1][idx2] == "B" and c_lst[idx-1][idx2+1] == "R":
                c_lst[idx][idx2] = "W"
            elif c_lst[idx-1][idx2] == "W" and c_lst[idx-1][idx2+1] == "B":
                c_lst[idx][idx2] = "R"
            elif c_lst[idx-1][idx2] == "R" and c_lst[idx-1][idx2+1] == "W":
                c_lst[idx][idx2] = "B"

    print(c_lst[len(c)-1][0])


if __name__ == '__main__':
    main()
