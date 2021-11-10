def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C_var = set(A) | set(B)

    # 出力
    print(N-len(C_var))

if __name__ == '__main__':
    main()