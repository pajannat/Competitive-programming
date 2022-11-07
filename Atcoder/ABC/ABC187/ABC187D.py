N = int(input())
A_list = []
AB_sum = []
cnt = 0

for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    AB_sum.append(2*A+B)
AB_sum.sort(reverse=True)

sum_A = sum(A_list)
sum_B = 0

for i in range(N):
    if sum_A >= sum_B:
        sum_B += AB_sum[i]
        cnt += 1
    else:
        break

print(cnt)

