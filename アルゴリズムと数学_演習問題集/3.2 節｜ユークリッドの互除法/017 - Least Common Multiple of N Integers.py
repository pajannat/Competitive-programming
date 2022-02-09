def main():
    from sys import stdin
    input = stdin.readline

    import math

    def my_lcm(arg1, arg2, *args):
        arg_gcd = math.gcd(arg1, arg2)
        arg_lcm = arg1*arg2 // arg_gcd

        for x in args:
            arg_gcd = math.gcd(arg_lcm, x)
            arg_lcm = arg_lcm*x // arg_gcd
        return arg_lcm
    
    N = int(input())
    A = list(map(int, input().split()))

    lcm_A = my_lcm(*A)

    print(lcm_A)

if __name__ == '__main__':
    main()