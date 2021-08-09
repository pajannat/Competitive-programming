def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    s = set()
    flg = False
    for i in range(N):
        Si = input().rstrip()
        if Si[0] == "!":
            if Si[1:] in s:
                print(Si[1:])
                flg = True
                break
            else:
                s.add(Si)
        else:
            if "!"+Si in s:
                print(Si)
                flg = True
                break
            else:
                s.add(Si)

    if not flg:
        print("satisfiable")
        
if __name__ == '__main__':
    main()