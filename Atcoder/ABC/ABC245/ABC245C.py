def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    flg = True
    X_bef = 0
    for i in range(1, N-1):
        # i==1のときだけ別に処理する。
        if i==1:
            if (abs(A[i-1]-A[i])<=K or abs(B[i-1]-A[i])<=K) and (abs(A[i+1]-A[i])<=K or abs(B[i+1]-A[i])<=K):
                X_bef = A[i]
            elif (abs(A[i-1]-B[i])<=K or abs(B[i-1]-B[i])<=K) and (abs(A[i+1]-B[i])<=K or abs(B[i+1]-B[i])<=K):
                X_bef = B[i]
            else:
                # 条件を満たすX[i]が見つからなかった場合
                flg = False
                break
        else:
            if abs(X_bef-A[i])<=K and (abs(A[i+1]-A[i])<=K or abs(B[i+1]-A[i])<=K):
                X_bef = A[i]
            elif abs(X_bef-B[i])<=K and (abs(A[i+1]-B[i])<=K or abs(B[i+1]-B[i])<=K):
                X_bef = B[i]
            else:
                X_bef = B[i-1]
                if abs(X_bef-A[i])<=K and (abs(A[i+1]-A[i])<=K or abs(B[i+1]-A[i])<=K):
                    X_bef = A[i]
                elif abs(X_bef-B[i])<=K and (abs(A[i+1]-B[i])<=K or abs(B[i+1]-B[i])<=K):
                    X_bef = B[i]
                else:
                    # 条件を満たすX[i]が見つからなかった場合
                    flg = False
                    break

    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()