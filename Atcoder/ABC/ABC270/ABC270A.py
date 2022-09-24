def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B = map(int, input().split())
    A_bin = [0, 0, 0]
    B_bin = [0, 0, 0]
    ans = 0

    # 処理
    def num_to_binlist(num, binlist):
        if num == 0:
            pass
        elif num == 1:
            binlist[0] = 1
        elif num == 2:
            binlist[1] = 1
        elif num == 3:
            binlist[0] = 1
            binlist[1] = 1
        elif num == 4:
            binlist[2] = 1
        elif num == 5:
            binlist[0] = 1
            binlist[2] = 1
        elif num == 6:
            binlist[1] = 1
            binlist[2] = 1
        elif num == 7:
            binlist[0] = 1
            binlist[1] = 1
            binlist[2] = 1
    
    num_to_binlist(A, A_bin)
    num_to_binlist(B, B_bin)

    for i in range(3):
        if A_bin[i] == 1 or B_bin[i] == 1:
            ans += 2**i


    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()