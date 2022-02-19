def main():
    from sys import stdin
    input = stdin.readline

    H = int(input())

    print( (H*(12800000+H))**(0.5) )
 
if __name__ == '__main__':
    main()