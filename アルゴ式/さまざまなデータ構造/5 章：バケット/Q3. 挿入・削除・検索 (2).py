def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    counter = [0 for _ in range(100001)]

    # Aにある数字をカウント
    for a in A:
        counter[a] += 1

    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            counter[int(query[1])] += 1

        # Delete query
        elif flg == 1:
            counter[int(query[1])] = 0

        # Count query
        elif flg == 2:
            print(counter[int(query[1])])


if __name__ == '__main__':
    main()