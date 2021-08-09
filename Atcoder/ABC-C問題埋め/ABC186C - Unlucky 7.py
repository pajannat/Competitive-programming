def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        str_i = str(i)
        oct_i = oct(i)
        if ('7' not in str_i) and ('7' not in oct_i):
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()