def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = [0]*(N+2)

    # いもす法(階差)で積雪を記録
    for i in range(Q):
        L, R, X = map(int, input().split())
        A[L] += X
        A[R+1] -= X

    # 累積をとり積雪値を復元
    AA = list(accumulate(A))

    # ansを作成
    ans = ""
    for i in range(1, N):
        if AA[i] > AA[i+1]:
            ans += ">"
        elif AA[i] == AA[i+1]:
            ans += "="
        elif AA[i] < AA[i+1]:
            ans += "<"

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()