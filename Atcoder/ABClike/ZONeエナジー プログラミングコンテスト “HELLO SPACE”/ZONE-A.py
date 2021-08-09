def main():
    from sys import stdin
    input = stdin.readline
    
    S = input().rsplit()
    S = S[0]
    print(S.count('ZONe'))            
    
if __name__ == '__main__':
    main()
