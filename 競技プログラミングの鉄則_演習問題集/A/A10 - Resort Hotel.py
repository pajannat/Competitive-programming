def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())
    L = [None] * D
    R = [None] * D
    for i in range(D):
        L[i], R[i] = map(int, input().split())
        L[i] -= 1
        R[i] -= 1

    P = [0] * N  # P[i] は A[0:i+1]の最大値
    Q = [0] * N  # Q[i] は A[i:]の最大値

    # 処理
    P[0] = A[0]
    for i in range(1, N):
        P[i] = max(P[i-1], A[i])

    Q[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        Q[i] = max(Q[i+1], A[i])
    
    # 答えを出力
    for i in range(D):
        LL = max(L[i]-1, 0)
        RR = min(R[i]+1, N-1)
        print(max(P[LL], Q[RR]))


if __name__ == '__main__':
    main()