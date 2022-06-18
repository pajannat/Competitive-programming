def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    koma = [-1 for i in range(N)]

    # 処理
    P = 0
    for i in range(N):
        # 操作1 コマを0に置く
        koma[i] = 0
        # 操作2 置かれているコマをAi進める
        # koma N個すべて見る
        for j in range(N):
            tmp = 0
            # コマが置かれている場合
            if koma[j] != -1:
                tmp = koma[j] + A[i]
                # マス3を超える場合
                if tmp >= 4:
                    P += 1
                    koma[j] = -1
                else:
                    koma[j] = tmp
    
    # 答えを出力
    print(P)


if __name__ == '__main__':
    main()