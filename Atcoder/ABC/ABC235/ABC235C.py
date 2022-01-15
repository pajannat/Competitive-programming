def main():
    from sys import stdin
    input = stdin.readline

    from collections import Counter

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    ans_dict = {}
    cnt_dict = {}

    for i in range(N):
        str_Ai = str(A[i])
        if str_Ai not in cnt_dict.keys():
            cnt_dict[str_Ai] = 1
        else:
            cnt_dict[str_Ai] += 1

        ans_dict[str_Ai+","+str(cnt_dict[str_Ai])] = i+1

    for i in range(Q):
        x, k = map(int, input().split())
        ans_key = str(x)+","+str(k)
        if ans_key in ans_dict:
            print(ans_dict[ans_key])
        else:
            print(-1)


if __name__ == '__main__':
    main()