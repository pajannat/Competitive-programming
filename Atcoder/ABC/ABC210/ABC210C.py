def main():
    from sys import stdin
    input = stdin.readline

    N, K = map(int, input().split())
    C_list = list(map(int, input().split()))
    cnt = {}
    max_sum = 0

    sum = 0
    for c in C_list:
        cnt[c] = 0

    # 区間0~Kに含まれる数の種類を数える
    for i in range(K):
        if cnt[C_list[i]] == 0:
            sum += 1
            cnt[C_list[i]] += 1
        else:
            cnt[C_list[i]] += 1
    max_sum = sum

    # 区間(i-K+1)~iに含まれる数の種類を数える
    for i in range(K, N):
        cnt[C_list[i-K]] -= 1
        if cnt[C_list[i-K]] == 0:
            sum -= 1

        if cnt[C_list[i]] == 0:
            sum += 1
            cnt[C_list[i]] += 1
        else:
            cnt[C_list[i]] += 1
        # 区間に含まれる数の種類 の最大数 を更新
        max_sum = max(max_sum, sum)

    print(max_sum)

if __name__ == '__main__':
    main()