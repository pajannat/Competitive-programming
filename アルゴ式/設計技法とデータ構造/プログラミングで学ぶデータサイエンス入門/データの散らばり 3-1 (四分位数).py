def calc_median(X):
    if len(X) % 2 == 0:
        median = (X[len(X)//2 - 1]+X[len(X)//2])/2
    else:
        median = X[(len(X)-1)//2]
    return median

# 入力値を受け取る
N = int(input())
A = list(map(int, input().split()))
A.sort()


# 答えを求める
if len(A) % 2 == 0:
    Q1 = calc_median(A[:len(A)//2])
    Q2 = calc_median(A)
    Q3 = calc_median(A[len(A)//2:])
else:
    Q1 = calc_median(A[:len(A)//2])
    Q2 = calc_median(A)
    Q3 = calc_median(A[len(A)//2 + 1:])


# 答えを出力
print(Q1, Q2, Q3)