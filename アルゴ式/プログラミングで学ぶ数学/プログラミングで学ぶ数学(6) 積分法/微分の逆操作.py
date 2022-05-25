# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 原始関数の係数を求める
B = [0]
for i in range(N+1):
    B.append(int(A[i]/(i+1)))

# 答えを出力
print(*B)