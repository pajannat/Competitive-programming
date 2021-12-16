# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
mean_A = sum(A) / len(A)
B = [a - mean_A for a in A]

# 答えを出力
print(*B)