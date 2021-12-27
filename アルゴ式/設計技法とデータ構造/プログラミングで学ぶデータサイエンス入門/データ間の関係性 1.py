# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
ave_A = sum(A) / len(A)
ave_B = sum(B) / len(B)

ans = min(ave_A, ave_B) / max(ave_A, ave_B)

# 答えを出力
print(ans)