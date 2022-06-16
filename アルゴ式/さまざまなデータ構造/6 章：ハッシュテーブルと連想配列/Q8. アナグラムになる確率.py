def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = list(input().split())

    # 処理
    counter = {}
    for s in S:
        s = list(s)
        s.sort()
        s = "".join(s)
        counter[s] = counter.get(s, 0) + 1
    
    # 答えを出力
    all_ptn = N*(N-1) // 2
    num = 0
    for key in counter.keys():
        key_cnt = counter[key]
        num += key_cnt*(key_cnt-1) // 2
    
    ans = num / all_ptn
    print(ans)


if __name__ == '__main__':
    main()