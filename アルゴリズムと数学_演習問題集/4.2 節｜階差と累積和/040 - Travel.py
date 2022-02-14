def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split()))
    M = int(input())

    # Aの累積和を求める
    AA = list(accumulate(A))

    # 答えを求める
    ans = 0
    for i in range(M):
        if i == 0:
            B_bef = int(input())-1
        else:
            B_now = int(input())-1
            ans += abs(AA[B_now]-AA[B_bef])
            B_bef = B_now

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()