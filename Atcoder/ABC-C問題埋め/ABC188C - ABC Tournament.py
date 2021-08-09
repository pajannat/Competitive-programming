def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    list_A = list(map(int,input().split()))

    win_list = list_A[:]
    for i in range(1,N+1):
        win_list_tmp = []
        for j in range(1,2**(N-i)+1):
            if i == N:
                win_list_tmp.append(min(win_list[2*j-2],win_list[2*j-1]))
            else:
                win_list_tmp.append(max(win_list[2*j-2],win_list[2*j-1]))
        win_list = win_list_tmp[:]
    print(list_A.index(win_list[0])+1)

if __name__ == '__main__':
    main()