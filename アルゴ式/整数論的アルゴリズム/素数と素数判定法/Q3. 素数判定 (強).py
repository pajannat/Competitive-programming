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
    flg = sosuhantei(N)


    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()