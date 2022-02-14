def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    T = int(input())
    N = int(input())
    A = [0]*(2*T+2)

    # 答えを求める
    ans = 0
    for i in range(N):
        L, R = map(int, input().split())
        # いもす法(階差)で記録
        A[2*L+1] += 1
        A[2*R+1] -= 1
    
    # 累積和をとり、従業員数を復元
    AA = list(accumulate(A))

    # 答えを出力
    for i in range(1, T+1):
        print(AA[2*i])


if __name__ == '__main__':
    main()