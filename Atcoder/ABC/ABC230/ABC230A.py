def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    if N >= 42:
        N += 1

    # 処理
    ans = ''
    if len(str(N)) >= 2:
        ans = 'AGC0' + str(N)
    else:
        ans = 'AGC00' + str(N)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()