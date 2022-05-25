# 入力を受け取る
N, ave_A, sigma_A, ave_B, sigma_B = map(int, input().split())

# 答えを求める
K = sigma_B / sigma_A

# 答えを出力
print(K)