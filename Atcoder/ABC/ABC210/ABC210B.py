def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    S = input().rstrip()

    cnt = -1
    for i, s in enumerate(S):
        if int(s) == 1:
            cnt = i
            break
    
    if cnt % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()