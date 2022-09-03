def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    rui_A = [0] + list(accumulate(A))

    sum_B_max = -10**18
    B = A[:M]
    sum_B = 0
    for i, b in enumerate(B):
        sum_B += (i+1)*b
    
    sum_B_max = max(sum_B_max, sum_B)

    # 処理
    # しゃくとり法
    for i in range(N):
        if i+M >= N:
            break
        sum_B = sum_B - (rui_A[i+M] - rui_A[i]) + M*A[i+M]
        
        sum_B_max = max(sum_B_max, sum_B)

    # 答えを出力
    print(sum_B_max)


if __name__ == '__main__':
    main()