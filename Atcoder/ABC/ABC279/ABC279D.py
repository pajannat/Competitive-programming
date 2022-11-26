def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    A, B = map(int, input().split())
    ans = 10**19

    # 処理
    x = (A/(2*B))**(2/3) - 1
    x = int(x)
    for n in range(max(0,x-10), x+10):
        t = B*n + A/(math.sqrt(n+1))
        ans = min(ans, t)

    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()