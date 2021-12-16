# 入力を受け取る
N, K = map(int, input().split())
H = list(map(int, input().split()))

# 答えを求める
ans = [h*K for h in H]

# 答えを出力
print(*ans)