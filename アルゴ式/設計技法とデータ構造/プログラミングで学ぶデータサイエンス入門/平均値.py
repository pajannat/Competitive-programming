# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
ans = sum(A)/N

# 答えを出力
print(ans)