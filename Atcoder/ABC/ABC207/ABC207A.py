def main():
    from sys import stdin
    input = stdin.readline

    input_list = list(map(int,input().split()))
    input_list.sort()
    ans = input_list[1] + input_list[2]
    
    print(ans)

if __name__ == '__main__':
    main()