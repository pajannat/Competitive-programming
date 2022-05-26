def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 処理

    # 処理前に配列Aを反転
    # 配列の先頭への処理は計算量が大きいため
    A.reverse()

    # queryに対する処理
    for _ in range(Q):
        query = list(map(int, input().split()))

        # push front query
        if query[0] == 0:
            v = query[1]
            A.append(v)

        # pop front query
        else:
            if len(A) == 0:
                print("Error")
            else:
                print(A.pop())


if __name__ == '__main__':
    main()