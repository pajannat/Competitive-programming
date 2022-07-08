# 入力を受け取る
# 強平衡二分木の高さH
H = int(input())

# 処理
# 高さ H である強平衡二分木の頂点数の最大値 ans_max
ans_min = 0
# 高さ H である強平衡二分木の頂点数の最小値 ans_min
ans_max = 0

# 高さ H である強平衡二分木の頂点数の最大値を計算
for i in range(H+1):
    ans_max += 2**i

# 高さ H である強平衡二分木の頂点数の最小値を計算
for i in range(H):
    ans_min += 2**i
ans_min += 1

# 答えを出力
print(ans_min, ans_max)