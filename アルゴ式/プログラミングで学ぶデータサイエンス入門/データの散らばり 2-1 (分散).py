# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
def calc_Variance(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp

V_A = calc_Variance(A)
V_B = calc_Variance(B)

# 答えを出力
if V_A < V_B:
    print("A")
elif V_A > V_B:
    print("B")
else:
    print("same")