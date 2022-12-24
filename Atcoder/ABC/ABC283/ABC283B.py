def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [None]*Q
    for i in range(Q):
        query[i] = list(map(int, input().split()))

    # 処理
    for q in query:
        if q[0] == 1:
            A[q[1]-1] = q[2]
        elif q[0] == 2:
            print(A[q[1]-1])


if __name__ == '__main__':
    main()