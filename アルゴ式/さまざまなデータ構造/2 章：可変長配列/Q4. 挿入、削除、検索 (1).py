def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 答えを出力
    for _ in range(Q):
        query = list(map(int, input().split()))
        # insert query
        if query[0] == 0:
            k = query[1]
            v = query[2]
            A.insert(k, v)

        # erase query
        elif query[0] == 1:
            k = query[1]
            A.pop(k)

        # count query
        else:
            v = query[1]
            print(A.count(v))


if __name__ == '__main__':
    main()