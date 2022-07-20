def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Mで割ったあまりがiである個数
    counter = [0 for _ in range(M)]

    # 処理
    for a in A:
        # Mで割った数がiである数をカウント
        counter[a%M] += 1
    
    # 差がMとなる組み合わせの数 ans
    ans = 0
    for cnt in counter:
        ans += cnt * (cnt - 1) // 2
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()