from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def calc_SD(nums_list):
    nums_mean = sum(nums_list) / len(nums_list)
    var = 0
    for num in nums_list:
        var += (num - nums_mean) ** 2
    var /= len(nums_list)
    SD = var ** 0.5
    return SD

# 入力を受け取る
input_list = []
num_list = []
for i in range(47):
    X, S = input().split()
    input_list.append([X, int(S)])
    num_list.append(int(S))

SD = calc_SD(num_list)
mean = sum(num_list) / len(num_list)

for i in range(47):
    SS = 50 + 10*(num_list[i]-mean) / SD
    SS = Decimal(str(SS)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    input_list[i].append(SS)

# 答えを出力
for i in range(47):
    print(input_list[i][0], input_list[i][2])