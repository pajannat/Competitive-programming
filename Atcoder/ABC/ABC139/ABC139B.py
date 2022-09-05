def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    A, B = map(int, input().split())

    # 処理
    # 1 + (A-1)*ans = B
    ans = math.ceil((B-1)/(A-1))
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()