def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split()))

    comb_cnt = 0
    vec_cnt = 0

    # 処理
    for i in range(1, N+1):
        A_i = A[i]
        j = A[i]
        A_j = A[j]
        if (i == A_i):
            comb_cnt += 1
        elif (A_i == j) and (A_j == i):
            vec_cnt += 1

    def cmb(n, r):
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2,r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1,r,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])

        return result


    if comb_cnt < 2:
        ans = (vec_cnt // 2)
    else:
        ans = (vec_cnt // 2) + cmb(comb_cnt, 2)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()