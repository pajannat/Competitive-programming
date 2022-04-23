def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()

    S_set = set()
    for s in S:
        S_set.add(s)
    
    flg = True

    if len(S) != len(S_set):
        flg = False
    
    if S.isupper():
        flg = False
    
    if S.islower():
        flg = False
    
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()