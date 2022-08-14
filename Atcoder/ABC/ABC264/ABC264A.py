def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    L, R = map(int, input().split())
    S = 'atcoder'

    # 処理
    
    # 答えを出力
    print(S[L-1:R])


if __name__ == '__main__':
    main()