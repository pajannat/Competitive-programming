def main():
    from sys import stdin
    input = stdin.readline

    
    # 入力を受け取る
    H, W = map(int, input().split())
    S = []
    ans = 0

    # 処理
    for _ in range(H):
        S.append(list(input().rstrip()))
    
    for s in S:
        for x in s:
            if x == "#":
                ans += 1
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()