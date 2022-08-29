def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    ans = N % 998244353
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()