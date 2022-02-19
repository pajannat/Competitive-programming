def main():
    from sys import stdin
    input = stdin.readline

    n = int(input())
    
    if n >= 5:
        print("Yes")
    else:
        if 2**n > n**2:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
