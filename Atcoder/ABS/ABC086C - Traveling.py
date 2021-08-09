def main():
    from sys import stdin
    import math
    input = stdin.readline
    N = int(input())

    # n×m行列の入力を2次元リストに格納
    A = [[]*3 for _ in range(N)]
    for idx in range(N):
        A[idx] = [int(i) for i in input().split()]
    
    flg = True
    for idx in range(N):
        if idx == 0:
            # 経過時間t(総移動距離)
            t = A[idx][0]
            # 最短移動距離l
            l = abs(A[idx][1])+abs(A[idx][2])
            if (t)<(l):
                flg = False
                break
            elif (t-l)%2 ==1:
                flg = False
                break
            else:
                pass
        else:
            # 経過時間t(総移動距離)
            t = A[idx][0]-A[idx-1][0]
            # 最短移動距離l
            l = abs(A[idx][1]-A[idx-1][1])+abs(A[idx][2]-A[idx-1][2])
            if (t)<(l):
                flg = False
                break
            elif (t-l)%2 ==1:
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