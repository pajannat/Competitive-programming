def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = [-1 for _ in range(N)]
    head = 0
    tail = 0

    # 処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Push query
        if flg == 0:
            v = int(query[1])
            A[tail] = v
            tail += 1
            if tail == N:
                tail = 0

        # Pop query
        elif flg == 1:
            A[head] = -1
            head += 1
            if head == N:
                head = 0
    
    # 答えを出力
    for i in range(N):
        print(A[i])


if __name__ == '__main__':
    main()