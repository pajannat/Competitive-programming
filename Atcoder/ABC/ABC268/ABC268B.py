# ABC268B
# 入力を受け取る
S = input().rstrip()
T = input().rstrip()
len_S = len(S)

# 処理
if len(S) > len (T):
    print('No')
    exit()
else:
    for i in range(len_S):
        if S[i] != T[i]:
            print('No')
            exit()

print('Yes')