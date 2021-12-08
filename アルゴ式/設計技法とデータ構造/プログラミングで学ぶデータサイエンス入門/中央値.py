# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを出力
A.sort(reverse=True)

if len(A) % 2 == 0:
    median = (A[N//2 - 1]+A[N//2])/2
else:
    median = A[(N-1)//2]

# 答えを出力
print(median)