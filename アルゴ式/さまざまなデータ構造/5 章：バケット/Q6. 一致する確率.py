def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    counter = [0 for _ in range(100001)]

    # リストAから2つとる組み合わせ(all_ptn)
    all_ptn = (N*(N-1))//2
    # リストAから2つ取ったときに同じ数字で場合
    same_ptn = 0

    # 処理
    # それぞれの数字がリストAに何回出現しているかカウント
    for a in A:
        counter[a] += 1
    
    # same_ptnの計算
    for num in counter:
        same_ptn += (num*(num-1))//2
    
    # 答えの計算
    ans = same_ptn / all_ptn
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()