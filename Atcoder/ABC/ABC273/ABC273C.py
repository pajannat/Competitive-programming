def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    A_origin_val = sorted(list(set(A)))
    len_A_origin_val = len(A_origin_val)
    dic = {}
    from collections import defaultdict
    ans = defaultdict(lambda: 0)

    # 処理
    for i, a in enumerate(A_origin_val):
        dic[a] = len_A_origin_val - (i + 1)

    for a in A:
        ans[dic[a]] += 1
    
    # 答えを出力
    for i in range(N):
        if i in ans:
            print(ans[i])
        else:
            print(0)


if __name__ == '__main__':
    main()