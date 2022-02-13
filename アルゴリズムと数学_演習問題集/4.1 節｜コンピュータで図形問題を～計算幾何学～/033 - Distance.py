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
    
    def gaiseki(AB, AC):
        ans = abs(AB[0]*AC[1]-AB[1]*AC[0])
        return ans

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    BA = list_sub(B, A)
    BC = list_sub(B, C)

    CA = list_sub(C, A)
    CB = list_sub(C, B)

    ans = 0
    if naiseki(BA, BC) < 0:
        ans = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    elif naiseki(CA, CB) < 0:
        ans = math.sqrt((A[0]-C[0])**2 + (A[1]-C[1])**2)
    else:
        ans = gaiseki(BA, BC) / math.sqrt(BC[0]**2 + BC[1]**2)
    
    print(ans)

if __name__ == '__main__':
    main()