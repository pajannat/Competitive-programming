def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    X = list(map(int, input().split()))
    sum_hp = 10**7

    # 処理
    # 各座標Pに対し (Xi - P)**2 の総和を計算する
    for P in range(1, 101):
        # tmp_sum_hp の初期化
        tmp_sum_hp = 0
        for x in X:
            # (Xi - P)**2 を計算して tmp_sum_hp に加算
            tmp_sum_hp += (x - P)**2
        
        # sum_hp, tmp_sum_hp の、より小さい方を採用
        sum_hp = min(sum_hp, tmp_sum_hp)
    
    # 答えを出力
    print(sum_hp)


if __name__ == '__main__':
    main()