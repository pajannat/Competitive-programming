def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # 処理
    # ニム和(すべての数でXOR)を計算する
    XOR_A = A[0]
    for i in range(1, N):
        XOR_A = XOR_A ^ A[i]
    
    # 答えを出力
    if XOR_A == 0:
        print("Second")
    else:
        print("First")


if __name__ == '__main__':
    main()