# 入力を受け取る
import statistics
N = int(input())
A = list(map(int, input().split()))

# 答えを出力
print(statistics.mean(A))