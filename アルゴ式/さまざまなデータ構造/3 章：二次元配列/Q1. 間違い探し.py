def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())

    S = [list(input().rstrip()) for _ in range(H)]
    T = [list(input().rstrip()) for _ in range(H)]

    cnt = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == T[h][w]:
                pass
            else:
                cnt += 1
    
    # 答えを出力
    print(cnt)

if __name__ == '__main__':
    main()