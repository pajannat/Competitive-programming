def main():
    from sys import stdin
    input = stdin.readline

    MOD = 998244353
    # 入力を受け取る
    N = int(input())

    num = [2, 3, 3, 3, 3, 3, 3, 3, 2]

    # i+2桁のときに、1~9各数字が先頭の場合がそれぞれ何通りあるか?
    # 2~N桁まで順に計算していく
    for i in range(N-2):
        tmp_num = num.copy()
        # 1~9が先頭の場合について何通りか順に計算
        for j in range(1, 10):
            if j == 1:
                num[1-1] = (tmp_num[1-1] + tmp_num[2-1])%MOD
            elif j == 9:
                num[9-1] = (tmp_num[9-1] + tmp_num[8-1])%MOD
            else:
                num[j-1] = (tmp_num[j-2] + tmp_num[j-1] + tmp_num[j])%MOD

    print(sum(num)%MOD)

if __name__ == '__main__':
    main()