def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # collections.deque　(キュー構造(双方向連結リスト))
    A = deque(A)

    # queryに対する処理
    for _ in range(Q):
        query = list(map(int, input().split()))

        # push front query
        if query[0] == 0:
            v = query[1]
            A.appendleft(v)

        # push back query
        elif query[0] == 1:
            v = query[1]
            A.append(v)

        # get query
        else:
            k = query[1]
            if k > len(A)-1:
                print("Error")
            else:
                print(A[k])


if __name__ == '__main__':
    main()