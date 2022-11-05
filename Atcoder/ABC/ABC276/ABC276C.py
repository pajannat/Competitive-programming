def main():
    from sys import stdin
    input = stdin.readline

    import copy

    # 入力を受け取る
    N = int(input())
    P = list(map(int, input().split()))

    # 処理
    # 後ろからPを見る
    tmp_i = -1
    tmp_P = -1
    for i in range(len(P)-1, 0, -1):
        if P[i-1] > P[i]:
            tmp_i = i-1
            tmp_P = P[i-1]
            break
    
    next_P = -1
    for i in range(tmp_i+1, len(P)):
        if P[i] < tmp_P:
            next_P = max(next_P, P[i])
    
    tmp_list = copy.copy(P[tmp_i:])
    tmp_list.remove(next_P)
    tmp_list.sort(reverse=True)
    
    ans = copy.copy(P[:tmp_i]) + [next_P] + tmp_list
    
    # 答えを出力
    print(*ans)


if __name__ == '__main__':
    main()