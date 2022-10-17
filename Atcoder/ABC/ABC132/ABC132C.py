def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    D = list(map(int, input().split()))

    # 処理
    D.sort()
    K_min = D[len(D)//2 - 1]
    K_max = D[len(D)//2]
    
    # 答えを出力
    print(K_max - K_min)


if __name__ == '__main__':
    main()