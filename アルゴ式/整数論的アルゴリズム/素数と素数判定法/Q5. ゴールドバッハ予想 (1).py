def main():
    from sys import stdin
    input = stdin.readline

    def sosuhantei(N):
        NisSosu = True
        if N < 2:
            NisSosu = False

        for i in range(2, N):
            if i*i > N:
                break
            if N % i == 0:
                NisSosu = False
        return NisSosu
    
    N = int(input())

    flg = False
    for i in range(2, N-1):
        p = i
        q = N-i
        flg_p = sosuhantei(p)
        flg_q = sosuhantei(q) 
        if flg_p and flg_q:
            print(p)
            flg = True
            break
    
    if flg:
        pass
    else:
        print(-1)

if __name__ == '__main__':
    main()