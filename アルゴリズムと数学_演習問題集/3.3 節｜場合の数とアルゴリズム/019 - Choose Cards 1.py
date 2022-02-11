def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    cnt_list = [0]*3
    for a in A:
        if a == 1:
            cnt_list[0] += 1
        elif a == 2:
            cnt_list[1] += 1
        else:
            cnt_list[2] += 1

    ans = cnt_list[0]*(cnt_list[0]-1)//2 + cnt_list[1]*(cnt_list[1]-1)//2 + cnt_list[2]*(cnt_list[2]-1)//2

    print(ans)

if __name__ == '__main__':
    main()