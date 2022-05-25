# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
not_N = 10 - N
not_like_nums = not_N ** 3

# 答えを求める
ans = 10**3 - not_like_nums

# 答えを出力
print(ans)