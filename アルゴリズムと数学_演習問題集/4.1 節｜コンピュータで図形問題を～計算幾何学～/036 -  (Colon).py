def main():
    from sys import stdin
    input = stdin.readline

    import math

    def dist_2points(A, B):
        ans = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
        return ans

    A, B, H, M = map(int, input().split())

    Hsita = 2.5*math.pi - H*math.pi/6 - (M/60)*(math.pi/6)
    Msita = 2.5*math.pi - math.pi*(M/30)

    AA = [A*math.cos(Hsita), A*math.sin(Hsita)]
    BB = [B*math.cos(Msita), B*math.sin(Msita)]

    ans = dist_2points(AA, BB)
    print(ans)

if __name__ == '__main__':
    main()