def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())

    set_list = [set() for _ in range(N)]

    # 処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Follow query
        if flg == 0:
            x, y = int(query[1]), int(query[2])
            set_list[y].add(x)

        # Unfollow query
        elif flg == 1:
            x, y = int(query[1]), int(query[2])
            set_list[y].discard(x)

        # CountSameFollowers query
        elif flg == 2:
            z = int(query[1])
            z_set = set_list[z]

            cnt = 0
            for s in set_list:
                if s == z_set:
                    cnt += 1

            print(cnt-1)


if __name__ == '__main__':
    main()