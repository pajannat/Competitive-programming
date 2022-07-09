def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    a, b, d = map(int, input().split())

    # 処理
    sita = math.pi * (d/180)
    A = a*math.cos(sita) - b*math.sin(sita)
    B = a*math.sin(sita) + b*math.cos(sita)
    
    # 答えを出力
    print(A, B)


if __name__ == '__main__':
    main()