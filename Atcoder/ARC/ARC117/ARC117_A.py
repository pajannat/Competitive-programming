def main():
    from sys import stdin
    input = stdin.readline
    A, B = map(int,input().split())
 
    Ea = [0]*A
    for idx in range(A):
        Ea[idx] = idx+1
 
    Eb = [0]*B
    for idx in range(B):
        Eb[idx] = -idx-1
    
    while True:
        if (sum(Ea)+sum(Eb)) == 0:
            print(*Ea,*Eb)
            break
 
        if (sum(Ea)+sum(Eb)) < 0:
            Ea[A-1] = Ea[A-1] -(sum(Ea)+sum(Eb))
            print(*Ea,*Eb)
            break
 
        if (sum(Ea)+sum(Eb)) > 0:
            Eb[B-1] = Eb[B-1] - (sum(Ea)+sum(Eb))
            print(*Ea,*Eb)
            break
 
        print(sum(Ea)+sum(Eb))
 
if __name__ == '__main__':
    main()