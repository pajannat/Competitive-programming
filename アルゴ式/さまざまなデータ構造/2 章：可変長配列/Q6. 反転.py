def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 処理

    # 答えを出力
    for _ in range(Q):
        query = list(map(int, input().split()))

        # reverse query
        if query[0] == 0:
            A.reverse()

        # push query
        elif query[0] == 1:
            v = query[1]
            A.append(v)

        # pop query
        else:
            if len(A) == 0:
                print("Error")
            else:
                print(A.pop())


if __name__ == '__main__':
    main()