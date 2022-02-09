def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    divisor_list = []

    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisor_list.append(i)
            divisor_list.append(N//i)
    
    for d in divisor_list:
        print(d)

if __name__ == '__main__':
    main()