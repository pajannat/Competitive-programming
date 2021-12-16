# 入力を受け取る
N, K = map(int, input().split())
H = list(map(int, input().split()))

# 答えを求める
X = [h*K for h in H]

def calc_var(nums):
    tmp = 0
    mean_nums = sum(nums) / len(nums)
    for num in nums:
        tmp += (num - mean_nums)**2
    tmp /= len(nums)
    return tmp

# 答えを出力
print(calc_var(X)/calc_var(H))