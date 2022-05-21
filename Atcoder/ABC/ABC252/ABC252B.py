def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B_idx = list(map(int, input().split()))
    B = []
    for i in B_idx:
        B.append(A[i-1])

    # 処理
    A_max = max(A)
    B_max = max(B)
    
    # 答えを出力
    if A_max == B_max:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()