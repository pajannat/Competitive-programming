def main():

    from collections import defaultdict

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    set_A = set(A)

    d = defaultdict(int)
    ans = 0

    # 処理
    for a in A:
        d[a] += 1
    
    for k in set_A:
        ans += (d[k] // 2)
    
    # 答えを出力
    print(ans)


if __name__ == "__main__":
    main()