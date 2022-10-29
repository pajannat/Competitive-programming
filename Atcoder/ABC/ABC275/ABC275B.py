def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B, C, D, E, F = map(int, input().split())

    # 処理
    A %= 998244353
    B %= 998244353
    C %= 998244353
    D %= 998244353
    E %= 998244353
    F %= 998244353

    ans = ((A*B*C) - (D*E*F)) % 998244353
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()