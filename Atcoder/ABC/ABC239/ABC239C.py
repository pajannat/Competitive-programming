def main():
    from sys import stdin
    input = stdin.readline

    x1, y1, x2, y2 = map(int, input().split())

    def dist2(x,y, a,b):
        tmp = (x-a)**2 + (y-b)**2
        return tmp

    flg = False
    for i in range(x1-2, x1+3):
        for j in range(y1-2, y1+3):
            kyori1 = dist2(x1,y1, i,j)
            kyori2 = dist2(x2,y2, i,j)
            if (kyori1 == kyori2) and (kyori1 == 5):
                flg = True

    for i in range(x2-2, x2+3):
        for j in range(y2-2, y2+3):
            kyori1 = dist2(x1,y1, i,j)
            kyori2 = dist2(x2,y2, i,j)
            if (kyori1 == kyori2) and (kyori1 == 5):
                flg = True
    
    if flg:
        print("Yes")
    else:
        print("No")

 
if __name__ == '__main__':
    main()