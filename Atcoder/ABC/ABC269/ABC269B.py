def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = [list(input().rstrip()) for i in range(10)]
    nums = []

    A = 0
    B = 0
    C = 0
    D = 0
    # 処理
    for i in range(10):
        tmp_num = []
        for j in range(10):
            if S[i][j] == '#':
                tmp_num.append([i, j])
        if len(tmp_num) != 0:
            nums.append(tmp_num)
    
    A = nums[0][0][0] + 1
    B = nums[-1][0][0] + 1
    C = nums[0][0][1] + 1
    D = nums[0][-1][1] + 1

    
    # 答えを出力
    print(A, B)
    print(C, D)


if __name__ == '__main__':
    main()