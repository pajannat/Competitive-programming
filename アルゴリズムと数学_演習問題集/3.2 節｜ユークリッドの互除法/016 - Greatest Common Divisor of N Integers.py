def main():
    from sys import stdin
    input = stdin.readline

    import math

    def my_gcd(arg1, arg2, *args):
        ans = math.gcd(arg1, arg2)
        for x in args:
            ans = math.gcd(ans, x)
        return ans
    
    N = int(input())
    A = list(map(int, input().split()))

    ans = my_gcd(*A)

    print(ans)

if __name__ == '__main__':
    main()