def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    # 単数値を桁に分割
    S = input().rstrip()
    A = [int(s) for s in S]

    # 処理
    ans = -1
    for i in range(10):
        if i not in A:
            ans = i
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()