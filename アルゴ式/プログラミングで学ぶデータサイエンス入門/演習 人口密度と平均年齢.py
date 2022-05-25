# 都道府県の数
N = 47

# 入力
data = [input().split() for _ in range(N)]
X = [d[0] for d in data]
S = [int(d[1]) for d in data]
p = [int(d[2]) for d in data]
a = [float(d[3]) for d in data]

GPD = [p[i] / S[i] for i in range(N)]

ave_GPD = sum(GPD) / N
ave_ave_age = sum(a) / N

kyobunsan = 0
for i in range(N):
    kyobunsan += (GPD[i]-ave_GPD)*(a[i]-ave_ave_age)
kyobunsan /= N

def calc_Variance(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    tmp = 0
    for num in nums_list:
        tmp += (num - nums_mean) ** 2
    tmp /= len(nums_list)
    return tmp

var_GPD = calc_Variance(GPD)
var_ave_age = calc_Variance(a)

ans = kyobunsan/(var_GPD**0.5 * var_ave_age**0.5)

# 答えを出力
print(ans)