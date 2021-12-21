# 入力を受け取る
N = int(input())
H = list(map(int, input().split()))

# 答えを求める
def calc_SD(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp ** 0.5

ave_H = sum(H) / len(H)
SD_H = calc_SD(H)

ans = [(h-ave_H)/SD_H for h in H]

# 答えを出力
print(*ans)