def main():
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

    for i in range(54, 1000):
        flg = sosuhantei(i)
        if flg:
            print(i)
            break

if __name__ == '__main__':
    main()