def main():
    from sys import stdin
    input = stdin.readline
    
    N = input().rstrip()
    N_num = int(N)
    N_digits = len(N)

    sum = 0
    for n in range(1,N_digits+1):
        comma_num = 0
        if n % 3 == 0:
            comma_num = int(n/3)-1
        else:
            comma_num = int(n//3)        
        if n == N_digits:
            sum += (N_num - pow(10,n-1)+1)*comma_num
        else:
            sum += (pow(10,n) - pow(10,n-1))*comma_num  
    print(sum)


if __name__ == '__main__':
    main()