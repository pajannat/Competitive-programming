# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
def calc_MD(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    nums_MD = 0
    for num in nums_list:
        nums_MD += abs(num - nums_mean)
    nums_MD /= len(nums_list)
    return nums_MD

MD_A = calc_MD(A)
MD_B = calc_MD(B)

# 答えを出力
if MD_A < MD_B:
    print("A")
elif MD_A > MD_B:
    print("B")
else:
    print("same")
