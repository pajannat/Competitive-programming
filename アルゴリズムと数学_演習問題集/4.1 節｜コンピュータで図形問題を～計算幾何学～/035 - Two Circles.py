def main():
    from sys import stdin
    input = stdin.readline

    import math

    def dist_AB(A, B):
        ans = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
        return ans

    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    A = [x1, y1]
    B = [x2, y2]

    dist12 = dist_AB(A, B)

    ans = -1
    if dist12 > r1+r2:
        ans = 5
    elif dist12 == r1+r2:
        ans = 4
    elif dist12 == max(r1, r2)-min(r1, r2):
        ans = 2
    elif dist12 < max(r1, r2)-min(r1, r2):
        ans = 1
    else:
        ans = 3

    print(ans)

if __name__ == '__main__':
    main()