# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
ave_A = sum(A) / N
ave_B = sum(B) / N

kyo_AB = 0
for i in range(N):
    kyo_AB += (A[i]-ave_A)*(B[i]-ave_B)
kyo_AB /= N

def calc_Variance(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp

var_A = calc_Variance(A)
var_B = calc_Variance(B)

ans = kyo_AB/(var_A**0.5 * var_B**0.5)

# 答えを出力
print(ans)