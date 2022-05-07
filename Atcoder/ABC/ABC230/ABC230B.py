def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()
    T = 'oxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxx'

    # 処理
    flg = False
    for i in range(10):
        if T[i:i+len(S)] == S:
            flg = True
    
    # 答えを出力
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()