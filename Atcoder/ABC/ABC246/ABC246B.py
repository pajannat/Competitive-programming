def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    A, B = map(int, input().split())

    # 処理
    if A == 0:
        if B > 0:
            print(0, 1)
        else:
            print(0, -1)
    elif B == 0:
        if A > 0:
            print(1, 0)
        else:
            print(-1, 0)
    else:
        sita = math.atan(B/A)
        x = math.cos(sita)
        y = math.sin(sita)
        print(x, y)

if __name__ == '__main__':
    main()