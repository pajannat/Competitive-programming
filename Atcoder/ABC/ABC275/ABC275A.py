def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    H = list(map(int, input().split()))

    # 処理
    h = -1
    idx = -1
    for i in range(N):
        if h < H[i]:
            h = H[i]
            idx = (i+1)
    
    # 答えを出力
    print(idx)


if __name__ == '__main__':
    main()