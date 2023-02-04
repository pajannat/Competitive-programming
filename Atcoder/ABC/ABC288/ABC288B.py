def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    S = [input().rstrip() for _ in range(N)]
    SS = S[:K]

    # 処理
    SS.sort()
    
    # 答えを出力
    for s in SS:
        print(s)


if __name__ == '__main__':
    main()