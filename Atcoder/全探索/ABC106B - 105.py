def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())

    cnt = 0
    for num in range(1,N+1,2):
        divisor_cnt = 0
        for idx in range(1,num+1): 
            if num % idx == 0:
                divisor_cnt += 1
        if divisor_cnt == 8:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()