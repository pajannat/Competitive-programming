def calc_median(X):
    if len(X) % 2 == 0:
        median = (X[len(X)//2 - 1]+X[len(X)//2])/2
    else:
        median = X[(len(X)-1)//2]
    return median

def calc_IQR(X):
    if len(X) % 2 == 0:
        Q1 = calc_median(X[:len(X)//2])
        Q3 = calc_median(X[len(X)//2:])
    else:
        Q1 = calc_median(X[:len(X)//2])
        Q3 = calc_median(X[len(X)//2 + 1:])
    return Q3-Q1


# 入力値を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

# 答えを求める
IQR_A = calc_IQR(A)
IQR_B = calc_IQR(B)

# 答えを出力
if IQR_A > IQR_B:
    print("B")
elif IQR_A == IQR_B:
    print("same")
else:
    print("A")