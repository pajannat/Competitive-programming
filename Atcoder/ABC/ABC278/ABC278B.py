def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, M = map(int, input().split())

    # 処理            
    # 1m ずつ 24h シミュレーションする
    for _ in range(60*24):
        # Hの下1桁目とMの上1桁目を入れ替えた時間が, 24h表記で存在するか判定
        # 存在する場合は出力してexit()
        H_str = str(H)
        M_str = str(M)
        if len(H_str) < 2:
            H_str = "0" + H_str
        if len(M_str) < 2:
            M_str = "0" + M_str
        
        H_str2 = H_str[0] + M_str[0]
        M_str2 = H_str[1] + M_str[1]

        if (0 <= int(H_str2) <= 23) and (0 <= int(M_str2) <= 59):
            print(H, M)
            exit()

        # M += 1
        M += 1
        # M = 60 になったら, H += 1, M = 0 にする
        if M == 60:
            H += 1
            M = 0
        if H == 24:
            H = 0


if __name__ == '__main__':
    main()