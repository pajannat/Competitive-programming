def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())
    cnt = 0

    # 処理
    bef = None
    for s in S[::-1]:
        cnt += 1
        if bef == "0" and s == "0":
            cnt -= 1
            bef = None
            continue
        bef = s
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()