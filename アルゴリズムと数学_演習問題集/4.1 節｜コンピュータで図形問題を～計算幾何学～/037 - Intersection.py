def main():
    from sys import stdin
    input = stdin.readline

    import math

    def list_sub(A, B):
        AB = []
        for i in range(len(A)):
            AB.append(B[i]-A[i])
        return AB

    def naiseki(AB, AC):
        sum_vec = 0
        for i in range(len(AB)):
            sum_vec += AB[i]*AC[i]
        return sum_vec

    def cross(BA, BC):
        ans = BA[0]*BC[1]-BA[1]*BC[0]
        return ans

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A[0] -= B[0]
    A[1] -= B[1]
    C = list(map(int, input().split()))
    C[0] -= B[0]
    C[1] -= B[1]
    D = list(map(int, input().split()))
    D[0] -= B[0]
    D[1] -= B[1]
    B = [0, 0]

    BA = list_sub(B, A)
    BC = list_sub(B, C)
    BD = list_sub(B, D)
    CD = list_sub(C, D)
    CA = list_sub(C, A)
    CB = list_sub(C, B)

    BAlen = math.sqrt(BA[0]**2+BA[1]**2)
    BClen = math.sqrt(BC[0]**2+BC[1]**2)
    BDlen = math.sqrt(BD[0]**2+BD[1]**2)
    crossBABC = cross(BA, BC)
    crossBABD = cross(BA, BD)
    crossCDCA = cross(CD, CA)
    crossCDCB = cross(CD, CB)

    # A,B,C,Dが直線状に並ぶ場合
    if crossBABC==0 and crossBABD==0 and crossCDCA==0 and crossCDCB==0:
        # Bを中心として、C,DのどちらかひとつがAと反対側にある場合
        if naiseki(BA, BC)*naiseki(BA, BD) <= 0:
            print("Yes")
        # Bを中心として、C,D両方とAが反対側にある場合
        elif naiseki(BA, BC) < 0:
            print("No")
        # Bを中心として、C,D両方とAが同じ側にある場合
        else:
            # Bを中心として、C,D両方がAより遠くにある場合
            if (BAlen < BClen) and (BAlen < BDlen):
                print("No")
            else:
                print("Yes")
    else:
        # ABでC,Dが分割される、かつ、CDでA,Bが分割される場合
        if (crossBABC*crossBABD<=0) and (crossCDCA*crossCDCB<=0):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()