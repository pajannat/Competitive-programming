# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
ave_A = sum(A) / N
ave_B = sum(B) / N

ans = 0
for i in range(N):
    ans += (A[i]-ave_A)*(B[i]-ave_B)
ans /= N

# 答えを出力
print(ans)
