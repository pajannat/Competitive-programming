def main():
    from sys import stdin
    input = stdin.readline

    from operator import itemgetter

    S = list(input().rstrip())
    N = int(input())
    ans = []

    for i in range(N):
        name = input().rstrip()
        name_num = ""
        for s in name:
            s_idx = S.index(s)
            if s_idx < 9:
                name_num += "0" + str(s_idx+1)
            else:
                name_num += str(s_idx+1)
        ans.append((name, name_num))
    
    ans.sort(key = itemgetter(1))

    for i in range(N):
        print(ans[i][0])


if __name__ == '__main__':
    main()