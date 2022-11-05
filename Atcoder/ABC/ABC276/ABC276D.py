def main():
    from sys import stdin
    input = stdin.readline

    # 3変数以上の最大公約数
    import math
    def my_gcd(arg1, arg2, *args):
        ans = math.gcd(arg1, arg2)
        for x in args:
            ans = math.gcd(ans, x)
        return ans

    import copy
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = copy.copy(A)
    cnt = 0

    # 処理
    # Ai を 2, 3 で割れる限り繰り返し割る
    for i in range(N):
        tmp_Ai = A[i]
        while tmp_Ai % 2 == 0:
            tmp_Ai = tmp_Ai // 2
        while tmp_Ai % 3 == 0:
            tmp_Ai = tmp_Ai // 3
        A[i] = tmp_Ai
    
    # すべての要素が同じ数字であれば目標達成可能
    ok_flg = True
    for i in range(N-1):
        if A[i] != A[i+1]:
            ok_flg = False
    
    
    # 目標達成不可である場合-1を出力して終了
    if ok_flg == False:
        print(-1)
        exit()

    dev_num_B = my_gcd(*B)
    for i in range(N):
        B[i] = B[i] // dev_num_B

    # Bi を 2, 3 で割れる限り繰り返し割る
    for i in range(N):
        tmp_Bi = B[i]
        while tmp_Bi % 2 == 0:
            tmp_Bi = tmp_Bi // 2
            cnt += 1
        while tmp_Bi % 3 == 0:
            tmp_Bi = tmp_Bi // 3
            cnt += 1
        B[i] = tmp_Bi
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()