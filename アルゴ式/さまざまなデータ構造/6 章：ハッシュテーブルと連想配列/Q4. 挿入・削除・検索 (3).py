def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(input().split())

    dict = {}
    for a in A:
        dict[a] = dict.get(a, 0) + 1

    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            T = query[1]
            dict[T] = dict.get(T, 0) + 1

        # Delete query
        elif flg == 1:
            T = query[1]
            if T in dict:
                del dict[T]

        # Count query
        elif flg == 2:
            T = query[1]
            print(dict.get(T, 0))


if __name__ == '__main__':
    main()