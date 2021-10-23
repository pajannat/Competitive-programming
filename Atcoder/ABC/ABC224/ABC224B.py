def main():
    from sys import stdin
    input = stdin.readline

    from itertools import combinations

    # 入力
    H, W = map(int, input().split())

    A = [[]*W for _ in range(H)]
    for idx in range(H):
        A[idx] = [int(i) for i in input().split()]

    i_list = list(combinations(range(H), 2))
    j_list = list(combinations(range(W), 2))

    flg = True
    for i in i_list:
        for j in j_list:
            if A[i[0]][j[0]] + A[i[1]][j[1]] <= A[i[1]][j[0]] + A[i[0]][j[1]]:
                pass
            else:
                flg = False
      
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")
    # print(ans)

if __name__ == '__main__':
    main()