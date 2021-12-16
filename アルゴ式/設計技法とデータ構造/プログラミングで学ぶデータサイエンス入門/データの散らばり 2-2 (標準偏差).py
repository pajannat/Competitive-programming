# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
def calc_Variance(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp

var_A = calc_Variance(A)
SD_A = var_A ** 0.5

# 答えを出力
print(var_A)
print(SD_A)