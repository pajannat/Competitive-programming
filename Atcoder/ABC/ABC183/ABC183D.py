def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, W = map(int, input().split())
    water = [0] * (2*10**5 + 2)
    gross_water = [0] * (2*10**5 + 2)

    # 処理
    # imos法
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    
    # 累積和を計算
    gross_water[0] = water[0]
    for i in range(len(water) - 1):
        gross_water[i+1] = gross_water[i] + water[i+1]


    # 答えを出力
    for num in gross_water:
        if num > W:
            print('No')
            exit()
    
    print('Yes')


if __name__ == '__main__':
    main()