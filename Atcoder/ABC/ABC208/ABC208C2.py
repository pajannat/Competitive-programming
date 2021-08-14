N, K = map(int, input().split())
A_list = list(map(int, input().split()))
# A_listのidxと値をペアにしたリスト(order_list)を作成。
# valueでsortするので、(A_listのvalue, A_listのidx)で作成。
order_list = [(A_list[i], i) for i in range(0, len(A_list))]
order_list.sort()
total_distribution_list = [0] * N

K_tmp = K

# K >= Nのとき、全員に1個ずつ配る(K < Nとなるまで)
if K_tmp >= N:
    total_distribution_list = list(
        map(lambda x: x + (K_tmp // N), total_distribution_list))
    K_tmp -= (K_tmp // N) * N

# K_tmpを優先順(order_listのidx順)に1個ずつ配る
for i in range(K_tmp):
    distribution_num = order_list[i][1]
    total_distribution_list[distribution_num] += 1

for num in total_distribution_list:
    print(num)