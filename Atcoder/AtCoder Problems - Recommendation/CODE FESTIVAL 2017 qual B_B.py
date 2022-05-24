def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    D_cnt = {}

    # 処理
    for i in range(N):
        if D[i] not in D_cnt.keys():
            D_cnt[D[i]] = 1
        else:
            D_cnt[D[i]] += 1
    
    flg = True
    for i in range(M):
        if T[i] in D_cnt.keys():
            if D_cnt[T[i]] >= 1:
                D_cnt[T[i]] -= 1
            else:
                flg = False
        else:
            flg = False

    # 答えを出力
    if flg:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()