def main():
    from sys import stdin
    input = stdin.readline
    
    N = int(input())

    cnt = 0
    for i in range(1,10**6+1):
        if int(str(i)*2) <= N:
            cnt += 1
        else:
            break

    print(cnt)

if __name__ == '__main__':
    main()