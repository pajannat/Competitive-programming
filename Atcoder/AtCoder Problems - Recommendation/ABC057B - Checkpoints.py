def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    AB_list = []
    CD_list = []
    for i in range(N):
        a, b = map(int, input().split())
        AB_list.append([a, b, 10**11, -1])
    
    for j in range(M):
        c, d = map(int, input().split())
        CD_list.append([c, d])

    for AB in AB_list:
        for idx, CD in enumerate(CD_list, 1):
            kyori = abs(AB[0]-CD[0]) + abs(AB[1]-CD[1])
            if kyori < AB[2]:
                AB[2] = kyori
                AB[3] = idx

    # 出力
    for AB in AB_list:
        print(AB[-1])

if __name__ == '__main__':
    main()