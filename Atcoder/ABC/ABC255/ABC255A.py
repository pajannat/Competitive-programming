def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    R, C = map(int, input().split())
    R, C = R-1, C-1
    A = [list(map(int, input().split())) for _ in range(2)]

    # 処理
    
    # 答えを出力
    print(A[R][C])


if __name__ == '__main__':
    main()