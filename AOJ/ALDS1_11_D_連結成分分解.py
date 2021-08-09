from sys import stdin
input = stdin.readline

from sys import setrecursionlimit
setrecursionlimit(100000000)  # RecursionError対策
    
N,M = map(int,input().split())
adj = [[] for _ in range(N)]
for m in range(1,M+1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
group_nums = [-1] * (N) 

def dfs(v,group_num):
    if group_nums[v] != -1: # すでに訪問済みなら終了
        return
    group_nums[v] = group_num
    for next in adj[v]: # 頂点vに隣接するv1,v2,...を探索
        dfs(next,group_nums[v])
    return

# すべてのnodeを開始点としてdfsで領域わけ
for idx in range(N):
    dfs(idx,idx)

Q_num = int(input())
for _ in range(Q_num):
    s,t = map(int,input().split())
    if group_nums[s] == group_nums[t] and group_nums[s] != -1:
        print("yes")
    else:
        print("no")