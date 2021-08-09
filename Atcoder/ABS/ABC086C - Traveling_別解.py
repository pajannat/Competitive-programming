def main():
    from sys import stdin
    import math
    input = stdin.readline
    N = int(input())
    t = [0]*110000
    x = [0]*110000
    y = [0]*110000
    t[0] = 0
    x[0] = 0
    y[0] = 0

    for idx in range(1,N+1):
        t[idx],x[idx],y[idx] = map(int,input().split())
    
    flg = True
    for idx in range(1,N+1):
        # 経過時間dt(総移動距離)
        dt = t[idx]-t[idx-1]
        # 距離l
        l = abs(x[idx]-x[idx-1])+abs(y[idx]-y[idx-1])
        if (dt)<(l):
            flg = False
            break
        elif (dt-l)%2 ==1:
            flg = False
            break
        else:
            pass

    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()