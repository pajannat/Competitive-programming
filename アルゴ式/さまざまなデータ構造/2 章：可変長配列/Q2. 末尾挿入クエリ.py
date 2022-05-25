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
        if query[0] == 0:
            k = query[1]
            # 配列外参照の場合はエラーメッセージを表示
            if k >= len(A):
                print("Error")
            else:
                print(A[k])
        else:
            v = query[1]
            A.append(v)


if __name__ == '__main__':
    main()