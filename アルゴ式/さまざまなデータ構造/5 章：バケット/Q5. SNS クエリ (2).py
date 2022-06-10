def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())

    # ユーザー i がユーザー j をフォローしていれば isfollow[i][j] = 1 とする 2 次元配列
    isfollow = [[0 for i in range(N)] for j in range(N)]
    # ユーザー i のフォロワーの数をバケットで管理
    counter = [0 for _ in range(N)]

    # 処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Follow query
        if flg == 0:
            x, y = int(query[1]), int(query[2])
            if isfollow[x][y] == 0:
                isfollow[x][y] = 1
                counter[y] += 1

        # Unfollow query
        elif flg == 1:
            x, y = int(query[1]), int(query[2])
            if isfollow[x][y] == 1:
                isfollow[x][y] = 0
                counter[y] -= 1

        # CountFollowers query
        elif flg == 2:
            z = int(query[1])
            print(counter[z])


if __name__ == '__main__':
    main()