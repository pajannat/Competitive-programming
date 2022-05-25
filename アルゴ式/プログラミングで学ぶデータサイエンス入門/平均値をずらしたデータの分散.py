# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
mean_A = sum(A) / len(A)
B = [a - mean_A for a in A]

def calc_Variance(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp

# 答えを出力
print(calc_Variance(B)/calc_Variance(A))