def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, X = map(int, input().split())
    AtoZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tmp = ""

    # 処理
    for s in AtoZ:
        tmp += s*N
    
    # 答えを出力
    print(tmp[X-1])


if __name__ == '__main__':
    main()