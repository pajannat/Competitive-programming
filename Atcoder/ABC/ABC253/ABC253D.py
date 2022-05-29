def main():
    from sys import stdin
    input = stdin.readline

    import math
    def my_lcm(x, y):
        return (x * y) // math.gcd(x, y)

    # 入力を受け取る
    N, A, B = map(int, input().split())
    AB_lcm = my_lcm(A, B)

    # 処理
    ans = (N*(1+N)) // 2
    ans -= ((N//A)*(A+A*(N//A))) // 2
    ans -= ((N//B)*(B+B*(N//B))) // 2
    ans += ((N//AB_lcm)*(AB_lcm+AB_lcm*(N//AB_lcm))) // 2

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()