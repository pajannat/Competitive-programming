def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # 処理
    cnt = 0
    for i in range(1, N):
        cnt = max(cnt, len(set(list(S[:i])) & set(list(S[i:]))))
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()