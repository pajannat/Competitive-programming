def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A_list = list(map(int,input().split()))
    A_list = sorted(A_list)

    B_list = [i for i in range(1,N+1)]

    if A_list == B_list:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()