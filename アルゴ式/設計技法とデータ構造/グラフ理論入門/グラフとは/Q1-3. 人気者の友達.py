# 入力を受け取る
N, M = map(int, input().split())

G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

popular_person_idx = 0
popular_person_friends_len = 0
for idx, g in enumerate(G):
    if len(g) > popular_person_friends_len:
        popular_person_friends_len = len(g) 
        popular_person_idx = idx

# G[popular_person_idx]をソート
G[popular_person_idx].sort()

# 答えを出力
print(*G[popular_person_idx])
