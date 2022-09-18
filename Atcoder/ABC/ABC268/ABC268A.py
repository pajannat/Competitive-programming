# ABC268A
# 入力を受け取る
num_list = list(map(int, input().split()))

# 処理
ans = 0
cnt_list = [0 for _ in range(101)]
for num in num_list:
    if cnt_list[num] == 0:
        ans += 1
    cnt_list[num] += 1

# 答えを出力
print(ans)