from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
A_list = list(map(int, input().split()))
# A_listの値とidxのペアをdictで保存。A_listの値をkeyとしてA_listのidxを参照できるように作成。
A_dict = {A_list[i]: i for i in range(0, len(A_list))}
A_sort = sorted(A_list)
num_list = [0] * N

K_tmp = K

# K >= Nのとき、全員に1個ずつ配る(K < Nとなるまで)
if K_tmp >= N:
    num_list = list(map(lambda x: x + (K_tmp // N), num_list))
    K_tmp -= (K_tmp // N) * N

# K_tmpを優先順に1個ずつ配る
for i in range(K_tmp):
    dist_num = A_dict[A_sort[i]]
    num_list[dist_num] += 1

for num in num_list:
    print(num)
