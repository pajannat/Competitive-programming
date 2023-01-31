def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, M, B = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0

    # 処理
    ans = M * sum(A) + N*M*B + N * sum(C)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()