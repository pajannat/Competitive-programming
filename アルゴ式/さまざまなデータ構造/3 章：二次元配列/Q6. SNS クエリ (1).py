def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())
    follow_list = [[] for _ in range(N)]

    # 処理
    for _ in range(Q):
        query = list(map(int, input().split()))
        flg = query[0]
        # Follow query
        if flg == 0:
            x, y = query[1], query[2]
            if x not in follow_list[y]:
                follow_list[y].append(x)

        # GetFollowers query
        if flg == 1:
            z = query[1]
            if len(follow_list[z]) == 0:
                print("No")
            else:
                follow_list[z].sort()
                print(*follow_list[z])


if __name__ == '__main__':
    main()