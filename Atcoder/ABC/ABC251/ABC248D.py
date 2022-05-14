def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    W = int(input())
    A = []

    # 処理
    for i in range(1, 100):
        A.append(i)
        A.append(i*100)
        A.append(i*10000)
    
    # 答えを出力
    print(len(A))
    print(*A)


if __name__ == '__main__':
    main()