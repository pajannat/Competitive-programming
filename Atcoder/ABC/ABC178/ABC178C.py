def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    ans = (10**N - (9**N + 9**N - 8**N)) % (10**9 + 7)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()