def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    ans = N

    # 処理
    ans = ans % K
    ans = min(ans, abs(ans - K))
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()