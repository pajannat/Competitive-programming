def main():
    from sys import stdin
    input = stdin.readline

    A = [3,1,4,1,5,9,2,6,5,3]
    # 入力を受け取る
    Q = int(input())

    # 答えを出力
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            print(A[query[1]])
        else:
            A[query[1]] = query[2]


if __name__ == '__main__':
    main()