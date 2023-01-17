def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    A, B = map(int, input().split())

    # 3変数以上の最大公約数
    def my_gcd(arg1, arg2, *args):
        ans = math.gcd(arg1, arg2)
        for x in args:
            ans = math.gcd(ans, x)
        return ans

    # 処理
    print(my_gcd(A, B))


if __name__ == '__main__':
    main()