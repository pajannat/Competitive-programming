def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    masu = []
    visited = [[0]*W for _ in range(H)]
    visited[0][0] = -1

    for _ in range(H):
        masu.append(list(input().rstrip()))

    # 処理
    I, J = 0, 0
    while True:
        # I, J が U かつ I != 0 の場合は上に1マス移動
        if masu[I][J] == 'U' and I != 0:
            I -= 1

        # I, J が D かつ I != H-1 の場合は下に1マス移動
        elif masu[I][J] == 'D' and I != H-1:
            I += 1

        # I, J が L かつ J != 0 の場合は左に1マス移動
        elif masu[I][J] == 'L' and J != 0:
            J -= 1

        # I, J が R かつ J != W-1 の場合は右に1マス移動
        elif masu[I][J] == 'R' and J != W-1:
            J += 1

        # いずれにも移動できなかった場合, ループ終了
        else:
            break

        # 移動先が既に訪問済みの場合, -1を出力してexit
        if visited[I][J] == -1:
            print(-1)
            exit()
        
        # visitedに移動先を記録
        visited[I][J] = -1

    # 答えを出力
    print(I+1, J+1)


if __name__ == '__main__':
    main()