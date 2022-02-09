def main():
    from sys import stdin
    input = stdin.readline

    import math

    N = int(input())

    divisor_list = []

    tmp_N = N
    for i in range(2, int(N**0.5)+1):
        while tmp_N % i == 0:
            divisor_list.append(i)
            tmp_N //= i
    
    tmp = math.prod(divisor_list)
    if N//tmp != 1:
        divisor_list.append(N//tmp)

    print(*divisor_list)

if __name__ == '__main__':
    main()