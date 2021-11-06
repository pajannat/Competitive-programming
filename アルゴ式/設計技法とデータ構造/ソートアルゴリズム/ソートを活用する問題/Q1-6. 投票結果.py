def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    # [番号, 得票数]
    seito = [[i, 0] for i in range(N)]

    for i in A:
        seito[i][1] += 1
    
    seito.sort(key=lambda x: x[1], reverse=True)

    # 出力
    for i, num in seito:
        print(i, num)

if __name__ == '__main__':
    main()