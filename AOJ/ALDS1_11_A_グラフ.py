def main():
    from sys import stdin
    input = stdin.readline
    
    N = int(input())
    Adj_mat = [[0]*N for _ in range(N)]
    for idx in range(N):
        Adj_idx = list(map(int,input().split()))
        for j in Adj_idx[1:]:
            if j == 0:
                break
            else:
                for k in Adj_idx[2:]:
                    Adj_mat[idx][k-1] = 1
                break
    for Adj in Adj_mat:
        print(*Adj)
    
if __name__ == '__main__':
    main()