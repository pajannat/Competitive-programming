def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    # 石が i 個のときの Grundy 数
    # 今回は0, 1, 2 のいずれか
    grundy = [0] * 100001

    # 処理
    # Grundy 数を求める
    for i in range(100001):
        # どの Grundy 数が使用済みか
        transit = [False, False, False]
        # 石が i-X 個のときの Grundy 数を使用済みとする
        if i >= X:
            transit[grundy[i-X]] = True
        # 石が i-Y 個のときの Grundy 数を使用済みとする
        if i >= Y:
            transit[grundy[i-Y]] = True
        
        # 0, 1, 2 のうち使用済みでない(最小の) Grundy 数が
        # 石 i 個のときの Grundy 数
        if transit[0] == False:
            grundy[i] = 0
        elif transit[1] == False:
            grundy[i] = 1
        else:
            grundy[i] = 2
    
    # すべての山について、ニム和を計算する
    XOR_grundy = 0
    for a in A:
        XOR_grundy = XOR_grundy ^ grundy[a]


    # 答えを出力
    if XOR_grundy == 0:
        print("Second")
    else:
        print("First")


if __name__ == '__main__':
    main()