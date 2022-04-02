def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    H, W = map(int, input().split())

    A = [list(map(int, input().split())) for i in range(H)]
    B = [list(map(int, input().split())) for i in range(H)]

    cnt = 0

    # 処理
    def mat_plus(A, i, j ,v):
        A[i][j] += v
        A[i+1][j] += v
        A[i][j+1] += v
        A[i+1][j+1] += v
    
    def mat_sub(A, i, j, v):
        A[i][j] -= v
        A[i+1][j] -= v
        A[i][j+1] -= v
        A[i+1][j+1] -= v

    # 0 <= i <= H-2, 0 <= j <= W-2 の範囲でAijをBijに合わせる
    for i in range(H-1):
        for j in range(W-1):
            BA_diff = B[i][j]-A[i][j]
            if BA_diff > 0:
                cnt += abs(BA_diff)
                mat_plus(A, i, j, abs(BA_diff))
            elif BA_diff < 0:
                cnt += abs(BA_diff)
                mat_sub(A, i, j, abs(BA_diff))
    
    # A, BのH行目とW列目が一致しているか判定
    flg = True
    for i in range(H):
        if A[i][-1] != B[i][-1]:
            flg = False

    for i in range(W):
        if A[-1][i] != B[-1][i]:
            flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
        print(cnt)
    else:
        print("No")

if __name__ == '__main__':
    main()