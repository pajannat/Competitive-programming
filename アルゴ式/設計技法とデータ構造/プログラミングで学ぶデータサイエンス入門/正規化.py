# 入力を受け取る
N = int(input())
H = list(map(int, input().split()))

# 答えを求める
min_H = min(H)
max_H = max(H)
range_H = max_H - min_H

X = list(map(lambda x:(x-min_H)/range_H, H))

# 答えを出力
print(*X)