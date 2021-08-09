def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())

    cnt = 0
    for n in range(1,N+1):
        str_n = str(n)
        if len(str_n) % 2 == 1:
            cnt +=1
    
    print(cnt)

if __name__ == '__main__':
    main()