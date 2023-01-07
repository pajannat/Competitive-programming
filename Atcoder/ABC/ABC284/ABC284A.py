def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = [input().rstrip() for _ in range(N)]

    # 処理
    
    # 答えを出力
    for i in range(N)[::-1]:
        print(S[i])


if __name__ == '__main__':
    main()