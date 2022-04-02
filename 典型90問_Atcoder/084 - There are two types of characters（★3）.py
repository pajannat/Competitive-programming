def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate
    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    L = []

    # 処理
    tmp_char = S[0]
    tmp_cnt = 1
    for i in range(1, N):
        if tmp_char == S[i]:
            tmp_cnt += 1
        else:
            L.append(tmp_cnt)
            tmp_cnt = 1
            tmp_char = S[i]
        
        if i == N-1:
            L.append(tmp_cnt)
    
    cumsum_L = list(accumulate(L))
    
    ans = 0
    for i in range(len(L)-1):
        if i == len(L)-1:
            ans += (L[i]*L[i+1])
        else:
            ans += L[i]*(cumsum_L[-1] - cumsum_L[i])
    
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()