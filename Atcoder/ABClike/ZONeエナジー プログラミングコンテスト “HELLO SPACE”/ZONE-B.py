def main():
    from sys import stdin
    input = stdin.readline
    
    N,D,H = map(int,input().split())
    kabe_list = []
    kabe = []
    
    for i in range(N):
        d, h = map(int, input().split())
        kabe.append([d, h])

    max_h = 0
    for k in kabe:
        dk,hk = k[0],k[1]
        takasa = (hk*D-H*dk)/(D-dk)
        max_h = max(max_h,takasa)
    print(max_h)             
    
if __name__ == '__main__':
    main()
