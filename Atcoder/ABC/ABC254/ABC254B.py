def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    ans_list = []

    # 処理
    for i in range(N):
        ans = []
        for j in range(i+1):
            if j == 0:
                ans.append(1)
            elif j == i:
                ans.append(1)
            else:
                a_ij = ans_list[i-1][j-1] + ans_list[i-1][j]
                ans.append(a_ij)
        print(*ans)
        ans_list.append(ans)


if __name__ == '__main__':
    main()