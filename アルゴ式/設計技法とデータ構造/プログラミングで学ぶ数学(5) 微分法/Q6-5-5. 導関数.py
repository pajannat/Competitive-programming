# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを格納
ans = []
for i in range(1,N+1):
    tmp = A[i] * i
    ans.append(tmp)

# 答えを出力
print(*ans)